import csv
import re
import argparse
import sys

from django.core.management.base import BaseCommand, CommandError
from domainmanager.models import CharacterProperty, Character,Property

# call by: python manage.py characterManager command=create character=1

class Command(BaseCommand):

    help = "Import and Cleanup of Genealogy"
    COMMAND_CREATE = "create"
    COMMAND_ADVANCE = "advance"
    COMMAND_DELETE = "delete"

    def add_arguments(self, parser):
        parser.add_argument('command', nargs='+', type=str)
        parser.add_argument('character', nargs='+', type=str)

    def handle(self, *args, **options):

        command = sys.argv[0]
        characterId = sys.argv[3]

        print("CharacterId: " + characterId)

        character = Character.objects.get(pk=int(characterId))

        for i in range(1,29):
            property = Property.objects.get(pk=i)
            cp = CharacterProperty(character=character, property=property)
            cp.save()