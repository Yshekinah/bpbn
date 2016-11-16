from django import template
from django.shortcuts import get_object_or_404
from django.template.base import Node
from django.utils.functional import allow_lazy

from domainmanager.logic import adminTools, characterTools
from domainmanager.models import Character, CharacterProperty, Event, News, Person, PropertyType

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
    xPCost = newValue * characterProperty.property.type.xpmultiplier

    if characterXP > xPCost:
        return {'characterproperty': characterProperty, 'xpCost': xPCost}
    else:
        pass


# Render the lvlUp Buttons while in character creation mode
@register.inclusion_tag('customTags/renderCharacterCreationButton.html')
def renderCharacterCreationButton(characterproperty_id):
    characterProperty = CharacterProperty.objects.get(pk=characterproperty_id)
    character = characterProperty.character

    raiseButton = False
    lowerButton = True
    border = 0
    treshold = 0
    initialProperties = 0
    characterAttributes = None

    if characterProperty.property.type.stattype in (PropertyType.STATUS.physical, PropertyType.STATUS.social, PropertyType.STATUS.mental):

        border = character.age_category.startingabilities
        if character.charactercreation.abilities < border:
            raiseButton = True

        if characterProperty.value == 1:
            lowerButton = False

    elif characterProperty.property.type.stattype in (PropertyType.STATUS.talents, PropertyType.STATUS.skills, PropertyType.STATUS.knowledges):
        border = character.age_category.startingskills
        if character.charactercreation.skills < border:
            raiseButton = True

        if characterProperty.value == 0:
            lowerButton = False

    elif characterProperty.property.type.stattype == PropertyType.STATUS.disciplines:
        border = character.age_category.startingdisciplines
        if character.charactercreation.disciplines < border:
            raiseButton = True

        if characterProperty.value == 0:
            lowerButton = False
    elif characterProperty.property.type.stattype == PropertyType.STATUS.influences:

        border = character.age_category.startinginfluences
        if character.charactercreation.influences < border:
            raiseButton = True

        if characterProperty.value == 0:
            lowerButton = False

    else:
        print("ERROR: Character creation exception - wanted to change: " + str(characterProperty) + " with freebies")

    return {'characterproperty': characterProperty, 'raiseButton': raiseButton, 'lowerButton': lowerButton}


# Render a section in the charactersheet: e.g. Skills, Physical or Disciplines
@register.inclusion_tag('customTags/renderCharacterSheetSection.html')
def renderCharacterSheetSection(sectionName, querySet, renderButton=True, showValue=True, maxValue=5, finished=True):
    return {'sectionName': sectionName, 'querySet': querySet, 'renderButton': renderButton, 'showValue': showValue, 'maxValue': maxValue,
            'finished': finished}


# Render the overview sections for the advanced characterCreatiojn option
@register.inclusion_tag('customTags/renderAdvancedCharacterCreationSection.html')
def renderAdvancedCharacterCreationSection(caption, borderValue, currentValue):
    return {'caption': caption, 'borderValue': borderValue, 'currentValue': currentValue}


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
        caption = 'PARAMATER name is missing AND param is unknown'

    return {'name': caption, 'command': command}


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


# Django has no built in subtraction method - which I needed for the charactersheet white dots
@register.filter
def subtract(value, arg):
    return value - arg


# Django has no built in range filter - which I needed for the character sheet black dots
@register.filter
def get_range(value):
    """
      Filter - returns a list containing range made from given value
      Usage (in template):

      <ul>{% for i in 3|get_range %}
        <li>{{ i }}. Do something</li>
      {% endfor %}</ul>

      Results with the HTML:
      <ul>
        <li>0. Do something</li>
        <li>1. Do something</li>
        <li>2. Do something</li>
      </ul>

      Instead of 3 one may use the variable set in the views
    """
    return range(value)


# Copied from: http://stackoverflow.com/questions/32201408/writing-py2-x-and-py3-x-compatible-code-without-six-text-type
# Left out the six module and used a str instead
@register.tag
def linebreakless(parser, token):
    nodelist = parser.parse(('endlinebreakless',))
    parser.delete_first_token()
    return LinebreaklessNode(nodelist)


class LinebreaklessNode(Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist

    def render(self, context):
        strip_line_breaks = allow_lazy(lambda x: x.replace('\n', ''), str)
        return strip_line_breaks(self.nodelist.render(context).strip())
