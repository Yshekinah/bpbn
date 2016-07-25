from django.shortcuts import get_list_or_404

from domainmanager.models import Property, CharacterProperty, CharacterDiscipline


def createInitialProperties(character):
    properties = Property.objects.filter(domain__exact=character.domain).filter(type__lte=2)

    for property in properties:
        cp = CharacterProperty(character=character, property=property, value=property.initial)
        cp.save()


def getCleanProperties(character):
    characterProperties = get_list_or_404(CharacterProperty, character=character)

    cleanProperties = {}

    # Add all character properties into a "clean" dict, so it can be accessed more easily
    for cproperty in characterProperties:
        cleanProperties[cproperty.property.name.replace(" ", "_")] = str(cproperty.value)
        # print("NAME: " + cproperty.property.name + ", VALUE: ", str(cproperty.value))

    return cleanProperties


def getCleanDisciplines(character):
    # Add all character disciplines into a "clean" dict, so it can be accessed more easily
    characterDisciplines = CharacterDiscipline.objects.all().filter(character=character).order_by('-level')

    cleanDisciplines = {}

    for cdiscipline in characterDisciplines:
        cleanDisciplines[cdiscipline.discipline.name] = cdiscipline.level
        # print("NAME: " + cdiscipline.discipline.name + ", VALUE: ", str(cdiscipline.level))

    return cleanDisciplines


def lvLUp(character):
    return "Not implemented... yet"
