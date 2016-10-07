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





                            # vName = re.sub('[!@#$]', '', column)
                            # vName = (re.sub('[^áÁéÉíÍöÖóÓoOüÜúÚuU0-9a-zA-Z\(\) ]+', '', vName))





            elif command == self.COMMAND_CLEANUP:
                vampire = Genealogy.objects.filter(generation__gte=2).order_by('-pk')
                for child in vampires:

                    print("Found name: " + child.name)
                    print("Found generation: " + str(child.generation))
                    print("Found columnStart: " + str(child.columnStart))
                    print("Found columnEnd: " + str(child.columnEnd))

                    fathers = Genealogy.objects.all().filter(generation=child.generation - 1).filter(columnStart__lte=child.columnStart).filter(
                        columnEnd__gte=child.columnEnd)
                    # .order_by('-columnStart')

                    for father in fathers:
                        print(">>>> Found Father: " + father.name)
                        print(">>>> Found Father generation: " + str(father.generation))
                        print(">>>> Found Father columnStart: " + str(father.columnStart))
                        print(">>>> Found Father columnEnd: " + str(father.columnEnd))
                        child.sire = father
                        child.save()
                        break

            elif command == self.COMMAND_DELETE:
                Genealogy.objects.all().delete()
