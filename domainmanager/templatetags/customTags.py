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
# calls renderCharacterSelection.html with queryset
# html renders the data
@register.inclusion_tag('customTags/characterSelection.html')
def renderCharacterSelection(id):
    player = get_object_or_404(Person, pk=id)
    characters = Character.objects.filter(player=player)
    return {'characters': characters}


# Render the lvlUp button in charactersheet
@register.inclusion_tag('customTags/renderLvlUpButton.html')
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


# Render the admin boons table: Current and already validated boons
@register.inclusion_tag('customTags/renderAdminBoonsTable.html')
def renderAdminBoonsTable(querySet):
    return {'querySet': querySet}

# Render the admin basket table: Current and already bought items
@register.inclusion_tag('customTags/renderAdminBasketTable.html')
def renderAdminBasketTable(querySet):
    return {'querySet': querySet}
