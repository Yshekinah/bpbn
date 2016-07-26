from django.shortcuts import get_list_or_404

from domainmanager.models import Property, CharacterProperty, ClanProperty

# Create initial character propertes
# 1 ... Abilites
# 2 ... Attributes
# 3 ... Backgrounds
def createInitialProperties(character):
    properties = Property.objects.filter(domain__exact=character.domain).filter(type__in=[1,2,3])

    for property in properties:
        cp = CharacterProperty(character=character, property=property, value=property.initial)
        cp.save()


def createInitialDisciplines(character):
    clanDisciplines = ClanProperty.objects.filter(clan__exact=character.clan)

    for discipline in clanDisciplines:
        cp = CharacterProperty(character=character, property=discipline.property, value=0)
        cp.save()


def getCleanCharacterProperties(character):
    characterProperties = get_list_or_404(CharacterProperty, character=character)

    cleanProperties = {}

    # Add all character properties into a "clean" dict, so it can be accessed more easily
    # PropertyType is not used
    for cproperty in characterProperties:
        cleanProperties[cproperty.property.name.replace(" ", "_")] = str(cproperty.value)

    return cleanProperties


def getCharacterDisciplines(character):
    characterDisciplines = CharacterProperty.objects.all().filter(character=character).filter(
        property__type__name__exact='Discipline')

    return characterDisciplines


def lvLUp(character):
    return "Not implemented... yet"
