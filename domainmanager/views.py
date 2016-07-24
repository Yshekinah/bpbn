from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404, get_list_or_404

from .forms import CharacterForm, CharacterPropertyFormSet
from .logic import characterTools
from .models import Character, Person, CharacterProperty, CharacterDiscipline, Clan, Vampire


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

    # players = Person.objects.all().order_by('lastname')
    characters = Character.objects.all()
    context = {'users': users, 'characters': characters,}

    return render(request, 'domainmanager/players.html', context)


@login_required()
def charactersheet(request, character_id):
    character = get_object_or_404(Character, pk=character_id)

    characterProperties = get_list_or_404(CharacterProperty, character=character)

    cleanProperties = {}

    # Add all character properties into a "clean" dict, so it can be accessed more easily
    for cproperty in characterProperties:
        cleanProperties[cproperty.property.name.replace(" ", "_")] = str(cproperty.value)
        # print("NAME: " + cproperty.property.name + ", VALUE: ", str(cproperty.value))

    # Add all character disciplines into a "clean" dict, so it can be accessed more easily
    characterDisciplines = CharacterDiscipline.objects.all().filter(character=character).order_by('-level')

    cleanDisciplines = {}

    for cdiscipline in characterDisciplines:
        cleanDisciplines[cdiscipline.discipline.name] = cdiscipline.level
        # print("NAME: " + cdiscipline.discipline.name + ", VALUE: ", str(cdiscipline.level))

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

    context = {'form':form, 'character':character}

    return render(request, 'domainmanager/characterinformation_edit.html', context)


@login_required()
def characterproperties_edit(request, character_id):
    character = Character.objects.get(pk=character_id)

    if request.method == "POST":
        characterForm = CharacterForm(request.POST)
        propertiesForm = CharacterPropertyFormSet(request.POST, request.FILES, instance=character)

        if characterForm.is_valid() and propertiesForm.is_valid():
            savedCharacter = characterForm.save()
            savedProperties = propertiesForm.save()
            return redirect('domainmanager:charactersheet', character_id)

    else:  # FUNKTIONIERT!
        characterForm = CharacterForm(instance=character)
        propertiesForm = CharacterPropertyFormSet(instance=character)
        # context = {'characterForm': characterForm, 'propertiesForm': propertiesForm}

    context = {'character': character, 'characterForm': characterForm, 'propertiesForm': propertiesForm}
    return render(request, 'domainmanager/characterinformation_edit.html', context)


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
