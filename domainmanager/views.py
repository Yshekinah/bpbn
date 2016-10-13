from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models import Sum
from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect

from .forms import *
from .logic import adminTools, characterTools
from .models import *


# , Boon, Character, CharacterShopping, Clan, Domain, Person, Property, PropertyType, Vampire, Xpearned, Xpspent


# handy decorator so only superusers and users who own the correspondng character
# are allowed to manipulate or view content regarding the character
def hasCharacter(func):
    def func_wrapper(request, character_id):

        characters = Character.objects.filter(player__pk=request.user.pk)
        found = False

        for character in characters:
            if str(character.pk) == character_id:
                found = True

        if found or request.user.is_superuser:
            return func(request, character_id)
        else:
            return render(request, 'domainmanager/base.html')

    return func_wrapper


@login_required()
def index(request):
    return render(request, 'domainmanager/base.html')


@login_required()
def characters(request):
    # Just get the main clans
    clans = Clan.objects.all().exclude(parent__isnull=False).order_by('name')

    # Just get the bloodlines
    bloodlines = Clan.objects.all().filter(parent__gte=1).order_by('name')

    if request.user.is_staff:
        characters = Character.objects.all().order_by('clan')
    else:
        characters = Character.objects.all().filter(domain=adminTools.getDomainFromPerson(request.user.id)).order_by('clan')

    context = {'clans': clans, 'bloodlines': bloodlines, 'characters': characters, }

    return render(request, 'domainmanager/characters.html', context)


@login_required()
def players(request):
    if request.user.is_staff:
        users = User.objects.all()
        characters = Character.objects.all().order_by('clan')
    else:
        users = User.objects.filter(domain=adminTools.getDomainFromPerson(request.user.id))
        characters = Character.objects.all().filter(domain=adminTools.getDomainFromPerson(request.user.id)).order_by('clan')

    context = {'users': users, 'characters': characters, }

    return render(request, 'domainmanager/players.html', context)


@login_required()
@hasCharacter
def charactersheet(request, character_id):
    character = get_object_or_404(Character, pk=character_id)

    physical = characterTools.getCharacterProportiesOfType(character, PropertyType.STATUS.physical)
    social = characterTools.getCharacterProportiesOfType(character, PropertyType.STATUS.social)
    mental = characterTools.getCharacterProportiesOfType(character, PropertyType.STATUS.mental)

    talents = characterTools.getCharacterProportiesOfType(character, PropertyType.STATUS.talents)
    skills = characterTools.getCharacterProportiesOfType(character, PropertyType.STATUS.skills)
    knowledges = characterTools.getCharacterProportiesOfType(character, PropertyType.STATUS.knowledges)

    merits = characterTools.getCharacterProportiesOfType(character, PropertyType.STATUS.merits)
    flaws = characterTools.getCharacterProportiesOfType(character, PropertyType.STATUS.flaws)
    disciplines = characterTools.getCharacterProportiesOfType(character, PropertyType.STATUS.disciplines)
    rituals = characterTools.getCharacterProportiesOfType(character, PropertyType.STATUS.rituals)
    thaumaturgicpaths = characterTools.getCharacterProportiesOfType(character, PropertyType.STATUS.thaumaturgicpaths)
    necromanticpaths = characterTools.getCharacterProportiesOfType(character, PropertyType.STATUS.necromanticpaths)
    influences = characterTools.getCharacterProportiesOfType(character, PropertyType.STATUS.influences)
    xpleft = characterTools.getXPforCharacter(character)
    xpearned = Xpearned.objects.filter(characters__in=[character]).aggregate(Sum('value'))['value__sum']

    if xpearned == None:
        xpearned = 0

    context = {'character': character, 'disciplines': disciplines, 'rituals': rituals,
               'thaumaturgicpaths': thaumaturgicpaths, 'necromanticpaths': necromanticpaths, 'xpleft': xpleft, 'xpearned': xpearned,
               'skills': skills, 'talents': talents, 'knowledges': knowledges, 'merits': merits, 'flaws': flaws, 'physical': physical,
               'social': social, 'mental': mental, 'influences': influences}

    request.session['active_character_id'] = character.pk
    request.session['active_character_name'] = character.firstname + " " + character.lastname
    request.session.modified = True

    return render(request, 'domainmanager/charactersheet.html', context)


@login_required()
def siresearch(request):
    context = {}

    if request.method == 'POST':

        searchparam = request.POST['search_text']
        # Search for characters with searchterm inside firstname, lastname or nickname
        # who are from the players domain
        # limit the results to 5
        characters = Character.objects.filter(
            Q(firstname__contains=searchparam) | Q(lastname__contains=searchparam) | Q(nickname__contains=searchparam)).filter(
            domain=adminTools.getDomainFromPerson(request.user.id))[:5]

        return render(request, 'domainmanager/customTags/sireResults.html', {'sires': characters})


# Create the character
@login_required()
def character_create(request):
    if request.method == "POST":

        form = CharacterFormCreate(request.POST)

        if form.is_valid():
            character = form.save()
            character.save()

            characterTools.createInitialProperties(character)
            characterTools.createInitialXP(character)

            return redirect('domainmanager:characters')
    else:

        form = CharacterFormCreate()

        # If user is admin give him special rights at character creation
        if request.user.is_superuser:
            print("Create character as super user")
        # if user is only "staff or player" restrict his rights
        else:
            form.fields['player'].queryset = Person.objects.filter(pk=request.user.id)
            person = get_object_or_404(Person, pk=request.user.id)
            form.fields['salutation'].queryset = Salutation.objects.filter(domain=person.domain)
            form.fields['sect'].queryset = Sect.objects.filter(domain=person.domain)
            form.fields['rank'].queryset = Rank.objects.filter(domain=person.domain)
            form.fields['gender'].queryset = Gender.objects.filter(domain=person.domain)
            form.fields['function'].queryset = PoliticalFuntion.objects.filter(domain=person.domain)
            form.fields['clan'].queryset = Clan.objects.filter(domain=person.domain).exclude(standardclan__exact=Clan.STATUS.restricted)
            form.fields['age_category'].queryset = AgeCategory.objects.filter(domain=person.domain)
            form.fields['domain'].queryset = Domain.objects.filter(pk=person.domain.id)
            form.fields['sire'].queryset = Character.objects.filter(domain=person.domain)

    return render(request, 'domainmanager/forms/character_create.html', {'form': form})


# Edit the character
@login_required()
@hasCharacter
def characterinformation_edit(request, character_id):
    character = get_object_or_404(Character, pk=character_id)

    if request.method == "POST":
        form = CharacterFormEdit(request.POST)

        if form.is_valid():
            character = form.save()
            character.save()
            return redirect('domainmanager:charactersheet', character_id)

    else:
        form = CharacterFormEdit(instance=character)

    context = {'form': form, 'character': character}

    return render(request, 'domainmanager/forms/characterinformation_edit.html', context)


@login_required()
@hasCharacter
def characterxps(request, character_id):
    character = get_object_or_404(Character, pk=character_id)

    xpEarned = Xpearned.objects.filter(characters__in=[character]).order_by('-timestamp')
    xpSpent = Xpspent.objects.filter(character=character).order_by('-timestamp')

    valueXpEarned = Xpearned.objects.filter(characters__in=[character]).aggregate(Sum('value'))['value__sum']
    valueXpSpent = Xpspent.objects.filter(character=character).aggregate(Sum('xpcost'))['xpcost__sum']

    context = {'character': character, 'xpSpent': xpSpent, 'xpEarned': xpEarned, 'valueXpEarned': valueXpEarned, 'valueXpSpent': valueXpSpent}
    return render(request, 'domainmanager/characterxps.html', context)


@login_required()
@hasCharacter
def characterboons(request, character_id):
    character = get_object_or_404(Character, pk=character_id)

    masterBoons = Boon.objects.filter(master=character).order_by('-timestamp')
    slaveBoons = Boon.objects.filter(slave=character).order_by('-timestamp')

    context = {'character': character, 'masterBoons': masterBoons, 'slaveBoons': slaveBoons}
    return render(request, 'domainmanager/characterboons.html', context)


@login_required()
@hasCharacter
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

            return redirect('domainmanager:characterboons', character_id)

    else:
        data = {'master': character}
        form = BoonForm(initial=data)
        form.fields['slave'].queryset = Character.objects.exclude(pk=character.pk).order_by('lastname')

    context = {'character': character, 'form': form}
    return render(request, 'domainmanager/forms/characterboon_create.html', context)


@login_required()
def characterboon_validation(request, boon_id, hash, answer):
    boon = get_object_or_404(Boon, pk=boon_id)
    returnToPersonId = 0

    if boon.hash_slave == hash:
        boon.approvedbyslave = answer
        returnToPersonId = boon.slave.pk

    if boon.hash_master == hash:
        boon.approvedbymaster = answer
        returnToPersonId = boon.master.pk

    boon.save()

    return redirect('domainmanager:characterboons', returnToPersonId)


@login_required()
@hasCharacter
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

            purchasedProperty.character = character
            purchasedProperty.hash_gm = characterTools.random_string(20)
            purchasedProperty.save()

        return redirect('domainmanager:characterbasket', character_id)

    else:

        form = CharacterShoppingForm()
        xpLeft = characterTools.getXPforCharacter(character)

        # Get all characterproperties from this character
        characterProperties = CharacterProperty.objects.filter(character=character)

        list = []
        for characterProperty in characterProperties:
            list.append(characterProperty.property.pk)

        # Remove all properties from the selectbox which the character already owns AND which are not too expsnsive to buy
        form.fields['property'].queryset = properties = Property.objects.exclude(id__in=list).filter(type__xpinitialprize__lte=xpLeft).order_by(
            'type')

        propertytypes = PropertyType.objects.all()

        form.fields['character'] = character

    context = {'character': character, 'form': form, 'properties': properties, 'propertytypes': propertytypes}
    return render(request, 'domainmanager/forms/charactershopping.html', context)


@login_required()
def charactershopping_cancel(request, character_id, item_id):
    adminTools.hasCharacter(request, character_id)

    item = get_object_or_404(CharacterShopping, pk=item_id)

    if item.approvedbygm == item.STATUS.waiting and str(item.character.id) == character_id:
        item.delete()

    return redirect('domainmanager:characterbasket', character_id)


@login_required()
@hasCharacter
def characterbasket(request, character_id):
    character = get_object_or_404(Character, pk=character_id)

    basket = CharacterShopping.objects.filter(character=character).order_by('-timestamp')

    context = {'character': character, 'basket': basket}
    return render(request, 'domainmanager/characterbasket.html', context)


@login_required()
def lvlup(request, characterproperty_id):
    characterProperty = CharacterProperty.objects.get(pk=characterproperty_id)
    character_id = characterProperty.character.pk
    characterProperties = CharacterProperty.objects.filter(pk=characterproperty_id)

    # Is it the correct user?
    if request.user.pk == characterProperty.character.player.pk:
        if characterTools.checkXP(characterProperty.character, characterProperties):
            characterProperty.value += 1
            characterProperty.save()

    return redirect('domainmanager:charactersheet', character_id)


@login_required()
@hasCharacter
def characteractions(request, character_id):
    character = get_object_or_404(Character, pk=character_id)

    downtimes = Downtime.objects.all()

    actions = Action.objects.filter(character=character)

    context = {'downtimes': downtimes, 'actions': actions, 'character': character}
    return render(request, 'domainmanager/characteractions.html', context)


@login_required()
def characteraction_edit(request, action_id):
    actionObject = get_object_or_404(Action, pk=action_id)

    if request.method == "POST":
        form = ActionForm(request.POST, request.FILES, instance=actionObject)

        if form.is_valid():
            action = form.save(commit=False)
            action.character = actionObject.character
            action.downtime = actionObject.downtime
            action.save()
            return redirect('domainmanager:characteractions', request.session['active_character_id'])

    else:
        form = ActionForm(instance=actionObject)

    context = {'form': form, 'action': actionObject}

    return render(request, 'domainmanager/forms/characteraction_edit.html', context)


@login_required()
@hasCharacter
def charactersecrets(request, character_id):
    character = get_object_or_404(Character, pk=character_id)

    characterSecrets = CharacterSecret.objects.filter(character=character).order_by('secret__rank')

    container = {}

    for characterSecret in characterSecrets:
        clan = characterSecret.secret.clan

        container.setdefault(clan.name, [])
        container[clan.name].append(characterSecret.secret)

    context = {'character': character, 'secrets': container}

    return render(request, 'domainmanager/charactersecrets.html', context)


@login_required()
def genealogy(request):
    return render(request, 'domainmanager/genealogy.html')


@login_required()
def genealogy2(request):
    return render(request, 'domainmanager/genealogy2.html')


#############################################################ADMINAREA#############################################################

@login_required()
@staff_member_required
def adminboons(request):
    # get only GM-WAITING & SLAVE-ACCEPTED boons - those the GM has to validate within his own dommain
    currentBoons = Boon.objects.filter(~Q(approvedbyslave__exact=Boon.STATUS.declined), Q(approvedbygm__exact=Boon.STATUS.waiting)) \
        .filter(slave__domain=adminTools.getDomainFromPerson(request.user.id)) \
        .order_by('-timestamp')

    # get the already validated boons for a log view
    oldBoons = Boon.objects.filter(Q(approvedbygm__exact=Boon.STATUS.accepted) | Q(approvedbygm__exact=Boon.STATUS.declined) | Q(
        approvedbyslave__exact=Boon.STATUS.declined)).filter(slave__domain=adminTools.getDomainFromPerson(request.user.id)).order_by('-timestamp')

    context = {'currentBoons': currentBoons, 'oldBoons': oldBoons}
    return render(request, 'domainmanager/adminboons.html', context)


@login_required()
@staff_member_required
def adminbasket(request):
    currentBasket = CharacterShopping.objects.filter(approvedbygm__exact=CharacterShopping.STATUS.waiting).filter(
        character__domain=adminTools.getDomainFromPerson(request.user.id)).order_by('-timestamp')
    oldBasket = CharacterShopping.objects.exclude(approvedbygm__exact=CharacterShopping.STATUS.waiting).filter(
        character__domain=adminTools.getDomainFromPerson(request.user.id)).order_by('-timestamp')

    context = {'currentBasket': currentBasket, 'oldBasket': oldBasket}
    return render(request, 'domainmanager/adminbasket.html', context)


@login_required()
@staff_member_required
def adminshopping_validation(request, property_id, hash, answer):
    property = get_object_or_404(CharacterShopping, pk=property_id)

    if property.hash_gm == hash:
        if int(answer) == property.STATUS.accepted:
            property.approvedbygm = property.STATUS.accepted
            property.save()

            # create a characterproperty and XP payment
            characterTools.addPropertytoCharacter(property, property.character)

        else:
            property.approvedbygm = property.STATUS.declined
            property.save()

    return redirect('domainmanager:adminbasket')


@login_required()
@staff_member_required
def adminboon_validation(request, boon_id, hash, answer):
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
    return redirect('domainmanager:index')
