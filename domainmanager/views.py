from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404

from .forms import CharacterForm, CharacterPropertyFormSet, CharacterFormCreate, BoonForm
from .logic import characterTools
from .models import Character, Person, Clan, Vampire, Xpearned, Xpspent, Boon


# Create your views here.

@login_required()
def index(request):
    return render(request, 'domainmanager/index.html')


@login_required()
def characters(request):
    clans = Clan.objects.all().exclude(parent__isnull=False).order_by('name')

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
    disciplines = characterTools.getCharacterDisciplines(character)

    context = {'character': character, 'properties': properties, 'disciplines': disciplines}

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

    return render(request, 'domainmanager/character_create.html', {'form': form})


# Edit the character
@login_required()
def characterinformation_edit(request, character_id):
    character = get_object_or_404(Character, pk=character_id)

    if request.method == "POST":
        form = CharacterForm(request.POST, instance=character)

        if form.is_valid():
            character = form.save()
            character.save()
            return redirect('domainmanager:charactersheet', character_id)
        else:
            print("ERROR!")
            for error in form.errors:
                print(error)
    else:
        form = CharacterForm(instance=character)

        properties = characterTools.getCleanCharacterProperties(character)

    context = {'form': form, 'character': character, 'properties': properties,}

    return render(request, 'domainmanager/characterinformation_edit.html', context)


@login_required()
def characterproperties_edit(request, character_id):
    character = get_object_or_404(Character, pk=character_id)

    if request.method == "POST":
        propertiesForm = CharacterPropertyFormSet(request.POST, request.FILES, instance=character)

        if propertiesForm.is_valid():

            savedProperties = propertiesForm.save(commit=False)

            lvlUpResult = characterTools.checkXP(character=character, characterProperties=savedProperties)

            if lvlUpResult == True:
                propertiesForm.save(commit=True)

                return redirect('domainmanager:charactersheet', character_id)
        else:
            for error in propertiesForm.errors:
                print(error)

    else:  # FUNKTIONIERT!
        propertiesForm = CharacterPropertyFormSet(instance=character)

    context = {'character': character, 'propertiesForm': propertiesForm}
    return render(request, 'domainmanager/characterproperties_edit.html', context)


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

    if boon.hash_gm == hash:
        if answer == "1":
            boon.approvedbygm = 'accepted'
        else:
            boon.approvedbygm = 'declined'

    if boon.hash_slave == hash:
        if answer == "1":
            boon.approvedbyslave = 'accepted'
        else:
            boon.approvedbyslave = 'declined'

    boon.save()

    return redirect('domainmanager:characterboonsummary', boon.slave.id)


@login_required()
def playersummary(request, player_id):
    player = get_object_or_404(Person, pk=player_id)

    characters = Character.objects.all().filter(pk=player_id)

    context = {'player': player, 'characters': characters}

    return render(request, 'domainmanager/playersummary.html', context)


@login_required()
def genealogy(request):
    vampires = Vampire.objects.all().filter(generation__lte="3").order_by('pk')

    context = {'vampires': vampires}

    return render(request, 'domainmanager/genealogy.html', context)
