from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect

from .forms import BoonForm, CharacterFormCreate, CharacterFormEdit, CharacterProperty, CharacterPropertyFormSet, CharacterShoppingForm
from .logic import adminTools, characterTools
from .models import Boon, Character, CharacterShopping, Clan, Person, Property, PropertyType, Vampire, Xpearned, Xpspent


# Create your views here.

@login_required()
def index(request):
    return render(request, 'domainmanager/index.html')


@login_required()
def characters(request):
    # Just get the main clans
    clans = Clan.objects.all().exclude(parent__isnull=False).order_by('name')

    # Just get the bloodlines
    bloodlines = Clan.objects.all().filter(parent__gte=1).order_by('name')

    characters = Character.objects.all().order_by('clan')

    context = {'clans': clans, 'bloodlines': bloodlines, 'characters': characters,}

    return render(request, 'domainmanager/characters.html', context)


@login_required()
def players(request):
    users = User.objects.all()

    characters = Character.objects.all()
    context = {'users': users, 'characters': characters,}

    return render(request, 'domainmanager/players.html', context)


@login_required()
def charactersheet(request, character_id):
    character = get_object_or_404(Character, pk=character_id)

    properties = characterTools.getCleanCharacterProperties(character)
    disciplines = characterTools.getCharacterProportiesOfType(character, PropertyType.STATUS.discipline)
    rituals = characterTools.getCharacterProportiesOfType(character, PropertyType.STATUS.ritual)
    thaumaturgicpaths = characterTools.getCharacterProportiesOfType(character, PropertyType.STATUS.thaumaturgicpath)
    necromanticpaths = characterTools.getCharacterProportiesOfType(character, PropertyType.STATUS.necromanticpath)
    xpleft = characterTools.getXPforCharacter(character)

    # getCharacterDisciplines(character)

    context = {'character': character, 'properties': properties, 'disciplines': disciplines, 'rituals': rituals,
               'thaumaturgicpaths': thaumaturgicpaths, 'necromanticpaths': necromanticpaths, 'xpleft': xpleft}

    request.session['active_character_id'] = character.pk
    request.session['active_character_name'] = character.firstname + " " + character.firstname
    request.session.modified = True

    return render(request, 'domainmanager/charactersheet.html', context)


# Create the character
@login_required()
def character_create(request):
    if request.method == "POST":

        form = CharacterFormCreate(request.POST)

        if form.is_valid():
            character = form.save()
            character.save()

            characterTools.createInitialProperties(character)
            characterTools.createInitialDisciplines(character)

            return redirect('domainmanager:characters')
    else:
        form = CharacterFormCreate()
        # No non-standard clans in character creation
        form.fields['clan'].queryset = Clan.objects.exclude(standardclan__exact=Clan.STATUS.restricted)

    return render(request, 'domainmanager/character_create.html', {'form': form})


# Edit the character
@login_required()
def characterinformation_edit(request, character_id):
    character = get_object_or_404(Character, pk=character_id)

    if request.method == "POST":
        form = CharacterFormEdit(request.POST, instance=character)

        if form.is_valid():
            character = form.save()
            character.save()
            return redirect('domainmanager:charactersheet', character_id)

    else:
        form = CharacterFormEdit(instance=character)

    properties = characterTools.getCleanCharacterProperties(character)
    context = {'form': form, 'character': character, 'properties': properties,}

    return render(request, 'domainmanager/characterinformation_edit.html', context)


# @login_required()
# def characterproperties_edit(request, character_id):
#     character = get_object_or_404(Character, pk=character_id)
#
#     if request.method == "POST":
#         propertiesForm = CharacterPropertyFormSet(request.POST, request.FILES, instance=character)
#
#         if propertiesForm.is_valid():
#
#             savedProperties = propertiesForm.save(commit=False)
#
#             lvlUpResult = characterTools.checkXP(character=character, characterProperties=savedProperties)
#
#             if lvlUpResult == True:
#                 propertiesForm.save(commit=True)
#
#                 return redirect('domainmanager:charactersheet', character_id)
#         else:
#             for error in propertiesForm.errors:
#                 print(error)
#
#     else:  # FUNKTIONIERT!
#         propertiesForm = CharacterPropertyFormSet(instance=character)
#
#     context = {'character': character, 'propertiesForm': propertiesForm}
#     return render(request, 'domainmanager/characterproperties_edit.html', context)


@login_required()
def characterxpsummary(request, character_id):
    character = get_object_or_404(Character, pk=character_id)

    xpEarned = Xpearned.objects.filter(character=character).order_by('-timestamp')
    xpSpent = Xpspent.objects.filter(character=character).order_by('-timestamp')

    context = {'character': character, 'xpSpent': xpSpent, 'xpEarned': xpEarned}
    return render(request, 'domainmanager/characterxpsummary.html', context)


@login_required()
def characterboonsummary(request, character_id):
    character = get_object_or_404(Character, pk=character_id)

    masterBoons = Boon.objects.filter(master=character).order_by('-timestamp')
    slaveBoons = Boon.objects.filter(slave=character).order_by('-timestamp')

    context = {'character': character, 'masterBoons': masterBoons, 'slaveBoons': slaveBoons}
    return render(request, 'domainmanager/characterboonsummary.html', context)


@login_required()
def characterboon_create(request, character_id):
    character = get_object_or_404(Character, pk=character_id)

    if request.method == 'POST':
        form = BoonForm(request.POST)

        if form.is_valid():
            boon = form.save(commit=False)
            boon.master = character
            boon.hash_gm = characterTools.random_string(20)
            boon.hash_slave = characterTools.random_string(20)
            boon.hash_master = characterTools.random_string(20)
            boon.save()

            return redirect('domainmanager:charactersheet', character_id)

    else:
        data = {'master': character}
        form = BoonForm(initial=data)

    context = {'character': character, 'form': form}
    return render(request, 'domainmanager/characterboon_create.html', context)


@login_required()
def characterboon_validation(request, boon_id, hash, answer):
    boon = get_object_or_404(Boon, pk=boon_id)

    if boon.hash_slave == hash:
        boon.approvedbyslave = answer

    if boon.hash_master == hash:
        boon.approvedbymaster = answer

    boon.save()

    return redirect('domainmanager:characterboonsummary', boon.slave.id)


@login_required()
def charactershopping(request, character_id):
    character = get_object_or_404(Character, pk=character_id)

    if request.method == 'POST':
        form = CharacterShoppingForm(request.POST)

        # As this form was not automatically created by a model
        # we also have to fill out the values manually
        if form.is_valid():
            purchasedProperty = CharacterShopping()
            if form.cleaned_data['property']:
                purchasedProperty.property = form.cleaned_data['property']
            if form.cleaned_data['newproperty']:
                purchasedProperty.newproperty = form.cleaned_data['newproperty']
            if form.cleaned_data['newpropertytype']:
                purchasedProperty.newpropertytype = form.cleaned_data['newpropertytype']

            purchasedProperty.character = character
            purchasedProperty.hash_gm = characterTools.random_string(20)
            purchasedProperty.save()

        return redirect('domainmanager:characterbasket', character_id)

    else:

        characterProperties = CharacterProperty.objects.filter(character=character)

        list = []
        for characterProperty in characterProperties:
            list.append(characterProperty.property.pk)

        form = CharacterShoppingForm()

        # Remove all properties from the selectbox which
        # the character already owns
        form.fields['property'].queryset = Property.objects.exclude(id__in=list).order_by('type')
        form.fields['character'] = character

    context = {'character': character, 'form': form}
    return render(request, 'domainmanager/charactershopping.html', context)


@login_required()
def characterbasket(request, character_id):
    character = get_object_or_404(Character, pk=character_id)

    basket = CharacterShopping.objects.filter(character=character).order_by('-timestamp')

    context = {'character': character, 'basket': basket}
    return render(request, 'domainmanager/characterbasket.html', context)


@login_required()
def playersummary(request, player_id):
    player = get_object_or_404(Person, pk=player_id)

    characters = Character.objects.all().filter(pk=player_id)

    context = {'player': player, 'characters': characters}

    return render(request, 'domainmanager/playersummary.html', context)


@login_required()
def lvlup(request, characterproperty_id):

    characterProperty = CharacterProperty.objects.get(pk = characterproperty_id)
    character_id = characterProperty.character.pk
    characterProperties = CharacterProperty.objects.filter(pk = characterproperty_id)

    characterTools.checkXP(characterProperty.character, characterProperties)
    characterProperty.value += 1
    characterProperty.save()

    return redirect('domainmanager:charactersheet', character_id)

@login_required()
def genealogy(request):
    vampires = Vampire.objects.all().filter(generation__lte="3").order_by('pk')

    context = {'vampires': vampires}

    return render(request, 'domainmanager/genealogy.html', context)


#############################################################ADMINAREA#############################################################

@login_required()
def adminboons(request):
    adminTools.checkAdmin(request)

    boons = Boon.objects.all().exclude(approvedbyslave__exact=Boon.STATUS.declined)

    context = {'boons': boons}
    return render(request, 'domainmanager/adminboons.html', context)


@login_required()
def adminbasket(request):
    adminTools.checkAdmin(request)

    basket = CharacterShopping.objects.filter(approvedbygm__exact=CharacterShopping.STATUS.waiting).order_by('-timestamp')

    context = {'basket': basket}
    return render(request, 'domainmanager/adminbasket.html', context)


@login_required()
def adminshopping_validation(request, property_id, hash, answer):
    adminTools.checkAdmin(request)
    property = get_object_or_404(CharacterShopping, pk=property_id)

    if property.hash_gm == hash:
        if answer == str(property.STATUS.accepted):
            property.approvedbygm = property.STATUS.accepted
            property.save()

            # handle property creation (if manually created) and XP payment
            adminTools.addPropertytoCharacter(property, property.character)

        else:
            property.approvedbygm = property.STATUS.declined
            property.save()

    return render(request, 'domainmanager/adminbasket.html')


@login_required()
def adminboon_validation(request, boon_id, hash, answer):
    adminTools.checkAdmin(request)
    boon = get_object_or_404(Boon, pk=boon_id)

    if boon.hash_gm == hash:
        if answer == str(boon.STATUS.accepted):
            boon.approvedbygm = boon.STATUS.accepted
        else:
            boon.approvedbygm = boon.STATUS.declined

    boon.save()

    return redirect('domainmanager:adminboons')


def logout(request):
    auth_logout(request)
    return render(request, 'domainmanager/base.html')