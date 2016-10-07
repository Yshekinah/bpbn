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
                vampires = []
                lineNumber = 0

                with open(filename, encoding='utf-8') as f:
                    reader = csv.reader(f, dialect=csv.excel, delimiter=';')
                    for row in reader:

                        if len(row):
                            sire = Genealogy.objects.filter(name=row[2])

                            clan = Clan.objects.filter(name=row[3], domain_id=1)

                            vampire = Genealogy(name=row[1])

                            if clan.exists():
                                vampire.clan = clan[0]

                            if sire.exists():
                                vampire.sire = sire[0]

                            vampire.save()

                        else:
                            print("WRONG: " + row)

            elif command == self.COMMAND_CLEANUP:
                vampires = Genealogy.objects.all().order_by('pk')

                filename = 'D:\\Stuff\\Django_projects\\bpbn_github\\bpbn\\genealogy_export.json'

                file = open(filename, 'w')
                file.write('var arr=[')

                for vampire in vampires:

                    file.write('\n{\n' + 'name:' + '\"' + vampire.name + '\"' + ',\n')
                    file.write('id:' + '\"' + str(vampire.pk) + '\"')
                    if vampire.sire:
                        file.write(',\n' + 'sire:' + '\"' + str(vampire.sire.pk) + '\"' + '\n')
                        file.write('},')
                    else:
                        file.write('\n' + '},')

                file.write('];')
                file.close()

            elif command == self.COMMAND_DELETE:
                Genealogy.objects.all().delete()
