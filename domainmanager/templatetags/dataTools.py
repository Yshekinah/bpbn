from django import template
from django.shortcuts import get_object_or_404

from domainmanager.logic import characterTools
from domainmanager.models import Character, CharacterProperty, Person

register = template.Library()


# user in characterboonsummary.html to get the
# triplets in STATUS array for the approvals
@register.filter
def getValue(array, key):
    return array[int(key)]


# Tag for character selection
# calls characterSelection.html with queryset
# html renders the data
@register.inclusion_tag('characterSelection.html')
def characterSelection(id):
    player = get_object_or_404(Person, pk=id)
    characters = Character.objects.filter(player=player)
    return {'characters': characters}


@register.inclusion_tag('renderLvlUpButton.html')
def renderLvlUpButton(characterproperty_id, oldValue, propName):
    characterProperty = CharacterProperty.objects.get(pk=characterproperty_id)

    characterXP = characterTools.getXPforCharacter(characterProperty.character)

    newValue = int(oldValue) + 1
    xPCost = 0

    xPCost = xPCost + (newValue * characterProperty.property.type.xpmultiplier)

    if characterXP > xPCost:
        return {'characterproperty': characterProperty, 'xpCost': xPCost}
    else:
        pass
