from django import template
from django.shortcuts import get_object_or_404

from domainmanager.logic import adminTools, characterTools
from domainmanager.models import Character, CharacterProperty, Event, News, Person

register = template.Library()

BUTTON_ACCEPT = 1
BUTTON_DECLINE = 2
BUTTON_THUMBS_UP = 3
BUTTON_THUMBS_DOWN = 4
BUTTON_NOTE = 5

DOMAIN_BUDAPEST = 1
DOMAIN_WARSAW = 2
DOMAIN_PRAHA = 3
DOMAIN_ZAGREB = 4


# DOMAIN_GRAZ = 5
# DOMAIN_VIENNA = 9

# user in characterboons.html to get the
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
def renderLvlUpButton(characterproperty_id, oldValue, propName=None):
    characterProperty = CharacterProperty.objects.get(pk=characterproperty_id)

    characterXP = characterTools.getXPforCharacter(characterProperty.character)

    newValue = int(oldValue) + 1
    xPCost = 0

    xPCost = xPCost + (newValue * characterProperty.property.type.xpmultiplier)

    if characterXP > xPCost:
        return {'characterproperty': characterProperty, 'xpCost': xPCost}
    else:
        pass


# Render a section in the charactersheet: e.g. Skills, Physical or Disciplines
@register.inclusion_tag('customTags/renderCharacterSheetSection.html')
def renderCharacterSheetSection(sectionName, querySet, renderButton=True, showXPCost=False):
    return {'sectionName': sectionName, 'querySet': querySet, 'renderButton': renderButton, 'showXPCost': showXPCost}


# Render the admin boons table: Current and already validated boons
@register.inclusion_tag('customTags/renderAdminBoonsTable.html')
def renderAdminBoonsTable(querySet):
    return {'querySet': querySet}


# Render the admin basket table: Current and already bought items
@register.inclusion_tag('customTags/renderAdminBasketTable.html')
def renderAdminBasketTable(querySet):
    return {'querySet': querySet}


# Render the Accept/Decline Button including the icons
@register.inclusion_tag('customTags/renderButton.html')
def renderButton(command, caption=None):
    if command == BUTTON_ACCEPT and caption == None:
        caption = 'Accept'

    if command == BUTTON_DECLINE and caption == None:
        caption = 'Decline'

    if command == BUTTON_THUMBS_UP and caption == None:
        caption = 'Mark as resolved'

    if command == BUTTON_THUMBS_DOWN and caption == None:
        caption = 'Mark as error'

    if command == BUTTON_NOTE and caption == None:
        caption = ''

    if caption == None:
        caption = 'PARAMATER caption is missing AND param is unknown'

    return {'caption': caption, 'command': command}


# Render the News section
@register.inclusion_tag('customTags/renderNews.html')
def renderNews(request):
    list = adminTools.getDomainsFromUserId(request.user.pk)

    news = News.objects.filter(domains__id__in=list).order_by('-validuntil')

    return {'news': news}


# Render the Calendar section
@register.inclusion_tag('customTags/renderCalendar.html')
def renderCalendar(request):
    events = Event.objects.all()

    return {'events': events}


# Render the corresponding CSS class for each domain event
@register.filter
def renderCalenderClassByDomain(domain_id):
    if domain_id == DOMAIN_BUDAPEST:
        return "event-success"

    if domain_id == DOMAIN_WARSAW:
        return "event-info"

    if domain_id == DOMAIN_PRAHA:
        return "event-important"

    if domain_id == DOMAIN_ZAGREB:
        return "event-special"
