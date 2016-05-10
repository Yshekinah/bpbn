import csv
import re
import argparse

from django.core.management.base import BaseCommand, CommandError
from domainmanager.models import Vampire

class Command(BaseCommand):

    help = "Import and Cleanup of Genealogy"
    COMMAND_IMPORT = "import"
    COMMAND_CLEANUP = "cleanup"
    COMMAND_DELETE = "delete"

    def add_arguments(self, parser):
        parser.add_argument('command', nargs='+', type=str)

    def handle(self, *args, **options):

        for command in options['command']:
            if command == self.COMMAND_IMPORT:

                filename = 'D:\Stuff\Django_projects\\bpbn\domainmanager\genealogy_new.csv'
                vampires = []
                lineNumber = 0
                columnNumber = 0

                # Vampire.objects.all().delete()

                with open(filename,mode='r') as csvfile:
                    line = csv.reader(csvfile, dialect='excel', delimiter=';')
                    for row in line:

                        lineNumber += 1
                        columnNumber = 0
                        vNameOld = ''

                        for column in row:
                            columnNumber += 1

                            if column != '' and column.find('generáció') == -1 and column.find('gener') == -1:
                                vName = re.sub('[!@#$]', '', column)

                                print(vName + " Generation: " + str(lineNumber) + " ColumnStart: " + str(columnNumber))

                                v = Vampire(name=vName, generation=lineNumber, columnStart=columnNumber)
                                v.save()

                                if vNameOld != '':
                                    vs = Vampire.objects.all().filter(name=vNameOld).order_by('-pk')[:1]
                                    for v in vs:
                                        v.columnEnd = columnNumber - 1
                                        v.save()

                                vNameOld = vName

            elif command == self.COMMAND_CLEANUP:
                vampires = Vampire.objects.all().filter(generation__gte=2).order_by('pk')
                for child in vampires:

                    print("Found name: " + child.name)
                    print("Found generation: " + str(child.generation))
                    print("Found columnStart: " + str(child.columnStart))
                    print("Found columnEnd: " + str(child.columnEnd))

                    fathers = Vampire.objects.all().filter(generation=child.generation-1).filter(columnStart__lte=child.columnStart).filter(columnEnd__gte=child.columnEnd)

                    for father in fathers:
                        print(">>>> Found Father: " + father.name)
                        print(">>>> Found Father generation: " + str(father.generation))
                        print(">>>> Found Father columnStart: " + str(father.columnStart))
                        print(">>>> Found Father columnEnd: " + str(father.columnEnd))
                        child.sire = father
                        child.save()

            elif command == self.COMMAND_DELETE:
                Vampire.objects.all().delete()

