from django.shortcuts import render

from domainmanager.models import CharacterProperty, Property, Xpspent


# are you an admin?
def checkAdmin(request):
    if request.user.groups.exclude(name='Admin').exists():
        return render(request, 'domainmanager/index.html')


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
