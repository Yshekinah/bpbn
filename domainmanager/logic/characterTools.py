import random
import string

from django.db import transaction
from django.db.models import Sum
from django.shortcuts import get_list_or_404

from domainmanager.models import CharacterProperty, ClanProperty, Property, Xpearned, Xpspent


# Create initial character properties
# property types are:
# 1 ... Abilities
# 2 ... Attributes
# 3 ... Backgrounds
def createInitialProperties(character):
    properties = Property.objects.filter(domain__exact=character.domain).filter(initalizeatcharactercreation__exact=Property.STATUS.yes)

    # initialze all initalizecharactercreation properties with value = 1
    for property in properties:
        cp = CharacterProperty(character=character, property=property, value=1)
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
                oldValue = property.tracker.previous('value')
                newValue = property.value
                xPCost = 0
                xPMultiplier = 0

                # New value must not be smaller than old value
                if newValue < oldValue:
                    raise ValueError()

                for i in range(oldValue + 1, newValue + 1):
                    xPCost = xPCost + (i * property.property.type.xpmultiplier)

                if characterXP < xPCost:
                    raise ValueError()

                xpSpentEntry = Xpspent(character=character, oldvalue=oldValue, newvalue=newValue,
                                       xpcost=xPCost, property=property.property)
                xpSpentEntry.save()

            return True

    except ValueError:

        return False


# Returns the current spendable XP of a character
def getXPforCharacter(character):
    xpearned = Xpearned.objects.filter(character=character).aggregate(Sum('value'))['value__sum']
    xpspent = Xpspent.objects.filter(character=character).aggregate(Sum('xpcost'))['xpcost__sum']

    return xpearned - xpspent


# Gives a random String with length
# used in creating a boon for security reasons
def random_string(length=20):
    pool = string.ascii_letters + string.digits
    return str(''.join(random.choice(pool) for i in range(length)))
