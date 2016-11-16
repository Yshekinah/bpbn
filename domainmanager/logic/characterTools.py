from django.db import transaction
from django.db.models import Sum
from django.shortcuts import get_object_or_404

from domainmanager.models import *


# Create initial character properties
# property types are:
# 1 ... Abilities
# 2 ... Attributes
# 3 ... Backgrounds
def createInitialProperties(character):
    # initialze all initalizecharactercreation==True properties
    properties = Property.objects.filter(domain__exact=character.domain).filter(initalizeatcharactercreation__exact=Property.STATUS.yes)

    for property in properties:

        value = 0

        # set value = 1 when they are attributes, as all other properties have to be bought with XP
        if property.type.stattype == PropertyType.STATUS.physical or \
                        property.type.stattype == PropertyType.STATUS.social or \
                        property.type.stattype == PropertyType.STATUS.mental:
            value = 1

        cp = CharacterProperty(character=character, property=property, value=value)
        cp.save()

    for discipline in character.clan.disciplines.all():
        cp = CharacterProperty(character=character, property=discipline, value=0)
        cp.save()


def createInitialSecrets(character):
    secrets = Secret.objects.filter(clan=character.clan).filter(rank__lte=character.age_category.startingsecrets)


# Used in charactersheet.html to display the values for each property type
def getCharacterProportiesOfType(character, type):
    return CharacterProperty.objects.filter(character=character).filter(
        property__type__stattype__exact=type).order_by('property__initalizeatcharactercreation')


# immer das nächste Level
# Skills * 3
# Backgrounds * 4
# Attribute * 5
# disci clan * 6 (without Mentor)
# disci clan * 5 (with Mentor)
# disci off clan * 7 (with Mentor)
def checkXP(character, characterProperties):
    # Get the current XPs for a character
    characterXP = getXPforCharacter(character)

    # Atomic because we can rollback if a player spent more xp than are available
    try:
        with transaction.atomic():
            for property in characterProperties:
                oldValue = property.value
                xPCost = 0

                xPCost = xPCost + ((oldValue + 1) * property.property.type.xpmultiplier)

                if characterXP < xPCost:
                    raise ValueError()

                xpSpentEntry = Xpspent(character=character, oldvalue=oldValue, newvalue=(oldValue + 1),
                                       xpcost=xPCost, property=property.property)
                xpSpentEntry.save()

            return True

    except ValueError:

        return False


# Returns the current spendable XP of a character
def getXPforCharacter(character):
    list = [character]

    xpearned = Xpearned.objects.filter(characters__in=[character]).aggregate(Sum('value'))['value__sum']
    xpspent = Xpspent.objects.filter(character=character).aggregate(Sum('xpcost'))['xpcost__sum']

    if xpearned == None:
        xpearned = 0

    if xpspent == None:
        xpspent = 0

    return xpearned - xpspent


# Gives a random String with length
# used in creating a boon for security reasons
def random_string(length=20):
    pool = string.ascii_letters + string.digits
    return str(''.join(random.choice(pool) for i in range(length)))


# give initial XP
def createInitialXP(character):
    xpearned = Xpearned(value=character.age_category.startingxp, note=str(character.age_category.startingxp) + " given at character creation")
    xpearned.save()
    xpearned.characters = [character]
    xpearned.save()


# A character bought a property:
# It was already approved by the gm and now it has to be added to charactersheet and spend his XP
def addPropertytoCharacter(property, character):
    characterProperty = CharacterProperty(character=character, property=property.property, value=1)
    characterProperty.save()

    if property.property.type.stattype == PropertyType.STATUS.flaws:
        xpearned = Xpearned(value=property.property.xpprize, note=str(property.property))
        xpearned.save()
        xpearned.characters.add(character)
        xpearned.save()
    elif property.property.type.stattype == PropertyType.STATUS.merits:
        xpSpent = Xpspent(oldvalue=0, newvalue=1, character=character, xpcost=property.property.xpprize, property=property.property)
        xpSpent.save()
    else:
        if property.mentor == True:
            xpcost = property.property.type.xpinitialprize - property.property.domain.mentorbonus
        else:
            xpcost = property.property.type.xpinitialprize

        xpSpent = Xpspent(oldvalue=0, newvalue=1, character=character, xpcost=xpcost, property=property.property)
        xpSpent.save()

# Change the value in characterCreation table corresponding to the raised or lowered value
def changeCharacterCreationValue(character_id, characterProperty, value):

    characterCreation = get_object_or_404(CharacterCreation, character_id=character_id)

    if characterProperty.property.type.stattype in (PropertyType.STATUS.physical, PropertyType.STATUS.social, PropertyType.STATUS.mental):
        characterCreation.abilities += value

    if characterProperty.property.type.stattype in (PropertyType.STATUS.skills, PropertyType.STATUS.talents, PropertyType.STATUS.knowledges):
        characterCreation.skills += value

    if characterProperty.property.type.stattype == PropertyType.STATUS.disciplines:
        characterCreation.disciplines += value

    if characterProperty.property.type.stattype == PropertyType.STATUS.influences:
        characterCreation.influences += value

    if characterProperty.property.type.stattype == PropertyType.STATUS.backgrounds:
        characterCreation.backgrounds += value

    if characterProperty.property.type.stattype == PropertyType.STATUS.secrets:
        characterCreation.secrets += value

    characterCreation.save()