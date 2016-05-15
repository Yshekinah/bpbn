from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404, get_list_or_404

from .models import Character, Person


# Create your views here.

def index(request):
    return HttpResponse("A beast I am, lest a beast I become!")


def charactersheet(request, character_id):
    character = get_object_or_404(Character, pk=character_id)

    context = {'character': character}

    return render(request, 'domainmanager/charactersheet.html', context)


def playersummary(request, player_id):
    player = get_object_or_404(Person, pk=player_id)

    characters = Character.objects.all().filter(pk=player_id)

    context = {'player': player, 'characters': characters}

    return render(request, 'domainmanager/playersummary.html', context)


def createCharacter(request):
    return HttpResponse('Have fun')
