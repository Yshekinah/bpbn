from domainmanager.models import Property, CharacterProperty


def createInitialProperties(character):
    properties = Property.objects.filter(domain__exact=character.domain).filter(type__lte=2)

    for property in properties:
        cp = CharacterProperty(character=character, property=property, value=property.initial)
        cp.save()

def lvLUp(character):
    return "Not implemented... yet"