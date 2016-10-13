import csv

from django.core.management.base import BaseCommand

from domainmanager.models import *


class Command(BaseCommand):
    help = "Import and Cleanup of Genealogy"
    COMMAND_IMPORT = "import"
    COMMAND_CLEANUP = "cleanup"
    COMMAND_DELETE = "delete"

    # Aufruf z.B.: python manage.py importGenealogy import

    def add_arguments(self, parser):
        parser.add_argument('command', nargs='+', type=str)

    def handle(self, *args, **options):

        for command in options['command']:
            if command == self.COMMAND_IMPORT:

                filename = 'D:\\Stuff\\Django_projects\\bpbn_github\\bpbn\\genealogy.csv'
                # structure
                # 0 ID; 1 NAME; 2 Sire; 3 Generation at embrace; 4 Current Generation; 5 Clan

                vampires = []
                lineNumber = 0

                with open(filename, encoding='utf-8') as f:
                    reader = csv.reader(f, dialect=csv.excel, delimiter=';')
                    for row in reader:

                        if len(row):
                            vampire = Genealogy(name=row[1])

                            sire = Genealogy.objects.filter(name=row[2])

                            initial_generation = row[3]

                            current_generation = row[4]

                            clan = Clan.objects.filter(name=row[5], domain_id=1)

                            domain = Domain.objects.filter(pk=1)

                            if clan.exists():
                                vampire.clan = clan[0]

                            if sire.exists():
                                vampire.sire = sire[0]

                            if domain.exists():
                                vampire.domain = domain[0]

                            if 'bloodline' not in initial_generation:
                                vampire.initial_generation = initial_generation
                            else:
                                vampire.initial_generation = sire[0].initial_generation

                            if 'bloodline' not in current_generation:
                                vampire.current_generation = current_generation
                            else:
                                vampire.current_generation = sire[0].current_generation

                            vampire.save()

                            # print(vampire)

                        else:
                            print("WRONG: " + row)

            elif command == self.COMMAND_CLEANUP:
                vampires = Genealogy.objects.all().order_by('pk')

                filename = 'D:\\Stuff\\Django_projects\\bpbn_github\\bpbn\\genealogy_export.json'

                file = open(filename, 'w')
                file.write('var data=[')

                for vampire in vampires:

                    file.write('\n{\n')

                    file.write('name:' + '\"' + vampire.name.replace('\n', ' ').replace('\"','\'') + '\"' + ',\n')

                    file.write('id:' + '\"' + str(vampire.pk) + '\"')

                    if vampire.sire:
                        file.write(',\n' + 'sire:' + '\"' + str(vampire.sire.pk) + '\"')

                    if vampire.initial_generation:
                        file.write(',\n' + 'initial_generation:' + '\"' + str(vampire.initial_generation) + '\"')

                    if vampire.current_generation:
                        file.write(',\n' + 'current_generation:' + '\"' + str(vampire.current_generation) + '\"')

                    if vampire.clan:
                        file.write(',\n' + 'clan:' + '\"' + str(vampire.clan.name) + '\"')

                    file.write('\n' + '},')

                file.write('];')
                file.close()

            elif command == self.COMMAND_DELETE:
                Genealogy.objects.all().delete()
