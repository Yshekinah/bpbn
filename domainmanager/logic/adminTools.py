from django.shortcuts import render

from domainmanager.models import Character, CharacterProperty, Domain, Property, Xpspent


# are you an admin?
def checkAdmin(request):
    if request.user.groups.exclude(name='Admin').exists():
        return render(request, 'domainmanager/index.html')

# Is this a valid user vs character combination
def userHasCharacter(request, character_id):
    characters = Character.objects.filter(player__pk=request.user.pk)
    found = False

    for character in characters:
        if str(character.pk) == character_id:
            found = True

    return found


# return a list with ids of all the players domains where he has characters
def getDomainsFromUserId(user_id):
    domains = Domain.objects.filter(character_domain__player=user_id)
    list = []
    for domain in domains:
        list.append(domain.pk)

    return list


# character C bought property P.
# It was approved by gm
# now we have to add it to him
def addPropertytoCharacter(property, character):
    isInBb = property.property != None

    if isInBb:
        characterProperty = CharacterProperty(character=character, property=property.property, value=1)
        characterProperty.save()

        xpSpent = Xpspent(oldvalue=0, newvalue=1, character=character, xpcost=property.property.type.xpinitialprize, property=property.property)
        xpSpent.save()

    else:
        newProperty = Property(name=property.newproperty, type=property.newpropertytype, initalizeatcharactercreation=Property.STATUS.no,
                               domain=character.domain)
        newProperty.save()
        characterProperty = CharacterProperty(character=character, property=newProperty, value=1)
        characterProperty.save()

        xpSpent = Xpspent(oldvalue=0, newvalue=1, character=character, property=newProperty, xpcost=property.newpropertytype.xpinitialprize)
        xpSpent.save()
