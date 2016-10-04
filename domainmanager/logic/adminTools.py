from django.shortcuts import get_object_or_404
from django.shortcuts import render

from domainmanager.models import Character, CharacterProperty, Domain, Person, Xpspent

# return a list with ids of all the players domains where he has characters
def getDomainsFromUserId(user_id):
    domains = Domain.objects.filter(character_domain__player=user_id)
    list = []
    for domain in domains:
        list.append(domain.pk)

    return list


# returns the domain the player (request.user.id) is bound to
def getDomainFromPerson(user_id):
    person = get_object_or_404(Person, pk=user_id)
    return person.domain


def hasCharacter(request, character_id):
    characters = Character.objects.filter(player__pk=request.user.pk)
    found = False

    for character in characters:
        if str(character.pk) == character_id:
            found = True

    if found or request.user.is_superuser:
        pass
    else:
        return render(request, 'domainmanager/base.html')
