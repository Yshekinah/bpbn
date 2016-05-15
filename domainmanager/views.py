from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404, get_list_or_404

from .models import Character, Person, CharacterProperty


# Create your views here.

def index(request):
    return HttpResponse("A beast I am, lest a beast I become!")


def charactersheet(request, character_id):
    character = get_object_or_404(Character, pk=character_id)

    characterproperties = get_list_or_404(CharacterProperty, character=character)

    cleanProperties = {}

    # Add all character properties into a "clean" dict, so it can be accessed more easily
    for cproperty in characterproperties:
        cleanProperties[cproperty.property.name.replace(" ", "_")] = str(cproperty.value)
        #print("NAME: " + cproperty.property.name + ", VALUE: ", str(cproperty.value))

    context = {'character': character, 'cleanProperties': cleanProperties}

    return render(request, 'domainmanager/charactersheet.html', context)


def playersummary(request, player_id):
    player = get_object_or_404(Person, pk=player_id)

    characters = Character.objects.all().filter(pk=player_id)

    context = {'player': player, 'characters': characters}

    return render(request, 'domainmanager/playersummary.html', context)


def createCharacter(request):
    return HttpResponse('Have fun')
