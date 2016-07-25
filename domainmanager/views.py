from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404

from .forms import CharacterForm, CharacterPropertyFormSet
from .logic import characterTools
from .models import Character, Person, Clan, Vampire


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

    cleanProperties = characterTools.getCleanProperties(character)

    cleanDisciplines = characterTools.getCleanDisciplines(character)

    context = {'character': character, 'cleanProperties': cleanProperties, 'cleanDisciplines': cleanDisciplines}

    return render(request, 'domainmanager/charactersheet.html', context)


# Create the character
@login_required()
def charactersheet_new(request):
    if request.method == "POST":

        form = CharacterForm(request.POST)

        if form.is_valid():
            character = form.save()
            character.save()

            characterTools.createInitialProperties(character)

            return redirect('domainmanager:characters')
    else:
        form = CharacterForm()

    return render(request, 'domainmanager/charactersheet_new.html', {'form': form})


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

    cleanProperties = characterTools.getCleanProperties(character)
    cleanDisciplines = characterTools.getCleanDisciplines(character)

    context = {'form': form, 'character': character, 'cleanProperties': cleanProperties,
               'cleanDisciplines': cleanDisciplines}

    return render(request, 'domainmanager/characterinformation_edit.html', context)


"""
def characterproperties_edit(request, character_id):
    character = get_object_or_404(Character, pk=character_id)

    if request.method == "POST":
        characterForm = CharacterForm(request.POST, instance=character)

        if CharacterForm.is_valid():
            savedCharacter = CharacterForm.save()
            return redirect('domainmanager:charactersheet', character_id)

    else:
        characterForm = CharacterForm(instance=character)
        characterPropertiesForm = CharacterPropertiesForm(instance=character)

    context = {'character': character, 'characterForm': characterForm, 'characterPropertiesForm': characterPropertiesForm}
    return render(request, 'domainmanager/characterproperties_edit.html', context)
"""


@login_required()
def characterproperties_edit(request, character_id):
    character = get_object_or_404(Character, pk=character_id)

    if request.method == "POST":
        # characterForm = CharacterForm(request.POST)
        propertiesForm = CharacterPropertyFormSet(request.POST, request.FILES, instance=character)

        if propertiesForm.is_valid():
            savedProperties = propertiesForm.save()
            return redirect('domainmanager:charactersheet', character_id)
        else:
            for error in propertiesForm.errors:
                print(error)

    else:  # FUNKTIONIERT!
        # characterForm = CharacterForm(instance=character)
        propertiesForm = CharacterPropertyFormSet(instance=character)
        # propertiesForm.fields['property'].widget = widgets.HiddenInput()
        # context = {'characterForm': characterForm, 'propertiesForm': propertiesForm}

    context = {'character': character, 'propertiesForm': propertiesForm}
    return render(request, 'domainmanager/characterproperties_edit.html', context)


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


@login_required()
def createCharacter(request):
    return HttpResponse('Have fun')
