import random
import string
from datetime import date
from time import strftime

from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from model_utils import Choices
from tinymce.models import HTMLField


def set_upload_directory_path(instance, filename):
    ctype = ContentType.objects.get_for_model(instance)
    length = 4
    pool = string.ascii_letters + string.digits
    #    app = ctype.app_label
    extension = filename.split('.')[-1]
    name = filename.split('.')[0]

    if ctype.model == 'action':
        return 'domain_{0}/{1}/'.format(instance.character.domain.id, ctype.model) + strftime('/%Y/%m/%d') + "/" + name + "_" + str(
            ''.join(random.choice(pool) for i in range(length))) + "." + extension
    elif ctype.model == 'domain':
        return 'domain_{0}/{1}/'.format(instance.pk, ctype.model) + strftime('/%Y/%m/%d') + "/" + name + "_" + str(
            ''.join(random.choice(pool) for i in range(length))) + "." + extension
    else:
        return 'domain_{0}/{1}/'.format(instance.domain.id, ctype.model) + strftime('/%Y/%m/%d') + "/" + name + "_" + str(
            ''.join(random.choice(pool) for i in range(length))) + "." + extension


class Country(models.Model):
    class Meta:
        verbose_name_plural = 'Countries'

    name = models.CharField(max_length=200)
    code = models.CharField(max_length=3)
    created = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)
    domain = models.ForeignKey('Domain', related_name='country_domain', default=1)

    def __str__(self):
        return self.name


class Salutation(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)
    domain = models.ForeignKey('Domain', default=1)

    def __str__(self):
        return self.name


class Gender(models.Model):
    name = models.CharField(max_length=25)
    domain = models.ForeignKey('Domain', default=1)
    created = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class AgeCategory(models.Model):
    class Meta:
        verbose_name_plural = 'Age categories'

    name = models.CharField(max_length=100)
    startingabilities = models.IntegerField(default=10)
    startingskills = models.IntegerField(default=20)
    startingdisciplines = models.IntegerField(default=4)
    startingbackgrounds = models.IntegerField(default=5)
    startinginfluences = models.IntegerField(default=4)
    startingxp = models.IntegerField(default=25)
    startingsecrets = models.IntegerField(default=4)
    lvluplimit = models.IntegerField(default=5)
    advancedlvluplimit = models.IntegerField(default=3)
    created = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)
    domain = models.ForeignKey('Domain', default=1)
    image = models.ImageField(upload_to=set_upload_directory_path, blank=True, null=True)

    def __str__(self):
        return self.name


class PoliticalFuntion(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)
    domain = models.ForeignKey('Domain', default=1)
    image = models.ImageField(upload_to=set_upload_directory_path, blank=True, null=True)

    def __str__(self):
        return self.name


# class Bloodline(models.Model):
#     name = models.CharField(max_length=100)
#     image = models.CharField(max_length=100, blank=True)
#     parent_clan = models.ForeignKey(Clan, blank=True, )
#
#     def __str__(self):
#         return self.name + " descending from " + self.parent_clan.name

# class Discipline(models.Model):
#     name = models.CharField(max_length=100)
#     clan = models.ForeignKey('Clan', related_name='clan')
#
#     def __str__(self):
#         return self.name


class Person(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    salutation = models.ForeignKey(Salutation)
    domain = models.ForeignKey('Domain', related_name='person_domain', default=1)
    country = models.ForeignKey(Country)
    image = models.ImageField(upload_to=set_upload_directory_path, blank=True, null=True)
    date_of_birth = models.DateField()
    description = HTMLField(blank=True)
    active = models.BooleanField(default=True)
    nickname = models.CharField(blank=True, null=True, max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):

        if self.user.is_superuser:
            return self.user.first_name + " " + self.user.last_name + " (SUPER), " + str(self.country)
        else:
            if self.user.is_staff:
                return self.user.first_name + " " + self.user.last_name + " (STAFF), " + str(self.country)
            else:
                return self.user.first_name + " " + self.user.last_name + ", " + str(self.country)


class Domain(models.Model):
    name = models.CharField(max_length=200)
    street = models.CharField(max_length=200, blank=True, null=True)
    postcode = models.CharField(max_length=10, blank=True, null=True)
    country = models.ForeignKey(Country, related_name='domain_country')
    gm = models.ForeignKey('Person', related_name='gm')
    substitute = models.ForeignKey('Person', related_name='substitute')
    schrecknetmessages = models.BooleanField(default=True)
    visions = models.BooleanField(default=True)
    secrets = models.BooleanField(default=True)
    boons = models.BooleanField(default=True)
    advancedcharactercreation = models.BooleanField(default=True)
    mentor = models.BooleanField(default=True)
    mentorbonus = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ]
    )
    influences = models.BooleanField(default=True)
    downtimes = models.BooleanField(default=True)
    image = models.FileField(upload_to=set_upload_directory_path, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Sect(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=set_upload_directory_path, blank=True, null=True)
    domain = models.ForeignKey(Domain, default=1)
    created = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Rank(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=set_upload_directory_path, blank=True, null=True)
    domain = models.ForeignKey(Domain, default=1)
    created = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=100, default="Insert event title")
    description = models.TextField()
    domain = models.ForeignKey(Domain)
    start_date = models.DateField()
    end_date = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Property(models.Model):
    class Meta:
        verbose_name_plural = 'Properties'

    STATUS = Choices((1, 'yes', 'Yes'), (2, 'no', 'No'))
    name = models.CharField(max_length=100)
    type = models.ForeignKey('PropertyType', related_name='type')
    description = models.TextField(default='please insert a useful manual text', blank=True, null=True)
    domain = models.ForeignKey(Domain, related_name='property_domain', default=1)
    initalizeatcharactercreation = models.IntegerField(choices=STATUS, default=STATUS.no, verbose_name="Initialize at character creation")
    xpprize = models.IntegerField(default=0, help_text='Only use XP costs here for merits and flaws! All other XP costs are set in property types')
    created = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Clan(models.Model):
    STATUS = Choices((1, 'standard', 'Standard clan'), (2, 'restricted', 'Restricted clan'))
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=set_upload_directory_path, blank=True, null=True)
    parent = models.ForeignKey('Clan', related_name='parentclan', blank=True, null=True)
    disciplines = models.ManyToManyField(Property, through='ClanProperty')
    standardclan = models.IntegerField(choices=STATUS, default=STATUS.standard)
    domain = models.ForeignKey(Domain, default=1)
    created = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class CharacterCreation(models.Model):
    class Meta:
        verbose_name_plural = 'Character creation entries'

    character = models.OneToOneField('Character', on_delete=models.CASCADE, )
    abilities = models.IntegerField(default=0)
    skills = models.IntegerField(default=0)
    disciplines = models.IntegerField(default=0)
    backgrounds = models.IntegerField(default=0)
    influences = models.IntegerField(default=0)
    secrets = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.character.firstname + " " + self.character.lastname + ", abilites: " + str(self.abilities) + ", skills: " + str(
            self.skills) + ", disc. " + str(self.disciplines)


class Character(models.Model):
    class Meta:
        verbose_name_plural = 'Characters'

    STATUS_visions = Choices((1, 'yes', 'Yes'), (2, 'no', 'No'))
    STATUS_active = Choices((1, 'active', 'Active'), (2, 'passive', 'Passive'))
    player = models.ForeignKey('Person', on_delete=models.CASCADE, default=1)
    salutation = models.ForeignKey(Salutation, default=1)
    nickname = models.CharField(max_length=200, blank=True)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200, blank=True, null=True)
    generation = models.IntegerField(
        default=12,
        validators=[
            MaxValueValidator(15),
            MinValueValidator(4)
        ]
    )
    schrecknetlevel = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ],
        help_text="What is the Schrecknet level of the character?",
        verbose_name='Schrecknet level'
    )
    clan = models.ForeignKey(Clan)
    sect = models.ForeignKey(Sect, default=1)
    date_of_birth = models.DateField(default=date.today)
    date_of_death = models.DateField(default=date.today)
    gender = models.ForeignKey(Gender, default=1)
    rank = models.ForeignKey(Rank, default=1)
    clan_rank = models.IntegerField(default=1)
    function = models.ForeignKey(PoliticalFuntion, default=6)
    age_category = models.ForeignKey(AgeCategory, default=1)
    willpower = models.IntegerField(default=5)
    humanity = models.IntegerField(default=5)
    frenzy = models.IntegerField(default=5)
    bloodpool = models.IntegerField(default=10)
    domain = models.ForeignKey('Domain', related_name='character_domain', default=1)
    active = models.IntegerField(choices=STATUS_active, default=STATUS_active.active)
    sire = models.CharField(max_length=250, blank=True, null=True)
    finished = models.BooleanField(default=False)
    levelup = models.BooleanField(default=False)
    quickedit = models.BooleanField(default=False)
    visionlevel = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ],
        help_text="What is the vision level of the character?",
        verbose_name='Vision level'
    )
    properties = models.ManyToManyField(Property, through='CharacterProperty')
    secretclan = models.ForeignKey(Clan, related_name='secretclan', blank=True, null=True)
    image = models.ImageField(upload_to=set_upload_directory_path, blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.salutation.name + " " + self.firstname + " " + self.lastname


class PropertyType(models.Model):
    STATUS = Choices((1, 'physical', 'Physical'),
                     (2, 'social', 'Social'),
                     (3, 'mental', 'Mental'),
                     (4, 'talents', 'Talents'),
                     (5, 'skills', 'Skills'),
                     (6, 'knowledges', 'Knowledges'),
                     (7, 'backgrounds', 'Backgrounds'),
                     (8, 'disciplines', 'Disciplines'),
                     (9, 'merits', 'Merits'),
                     (10, 'flaws', 'Flaws'),
                     (11, 'rituals', 'Rituals'),
                     (12, 'thaumaturgicpaths', 'Thaumaturgic Paths'),
                     (13, 'necromanticpaths', 'Necromantic Paths'),
                     (14, 'influences', 'Influences'),
                     (15, 'secrets', 'Secrets'))

    name = models.CharField(max_length=100)
    domain = models.ForeignKey('Domain', related_name='propertytype_domain', default=1)
    xpmultiplier = models.IntegerField(default=1)
    xpinitialprize = models.IntegerField(default=5)
    stattype = models.IntegerField(choices=STATUS, default=STATUS.talents)
    created = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ClanProperty(models.Model):
    class Meta:
        verbose_name_plural = 'clan properties'

    clan = models.ForeignKey(Clan)
    property = models.ForeignKey(Property, limit_choices_to={'type_id': PropertyType.STATUS.disciplines})
    created = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.clan.name + " " + self.property.name


class CharacterProperty(models.Model):
    class Meta:
        verbose_name_plural = 'Character properties'

    character = models.ForeignKey('Character', on_delete=models.CASCADE)
    property = models.ForeignKey('Property', on_delete=models.CASCADE)
    value = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ]
    )
    created = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.character.firstname + " " + self.character.lastname + ", " + self.property.name + ": " + str(self.value)


class CharacterShopping(models.Model):
    STATUS = Choices((1, 'waiting', 'Waiting'), (2, 'accepted', 'Accepted'), (3, 'declined', 'Declined'), (4, 'resolved', 'Resolved'),
                     (5, 'canceled', 'Canceled'))
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE, blank=True, null=True)
    mentor = models.BooleanField(default=False, help_text='Do you have access to a mentor?')
    approvedbygm = models.IntegerField(choices=STATUS, default=STATUS.waiting)
    hash_gm = models.CharField(max_length=20, default="")
    created = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.character.firstname + " " + self.character.lastname + " " + str(self.property)


class Downtime(models.Model):
    class Meta:
        verbose_name_plural = "Downtimes"

    name = models.CharField(max_length=200)
    description = models.CharField(max_length=250, blank=True, null=True)
    domain = models.ForeignKey('Domain', on_delete=models.CASCADE, null=True, blank=True)
    event = models.ForeignKey('Event', on_delete=models.CASCADE, null=True, blank=True)
    start = models.DateField()
    end = models.DateField()

    created = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    # https://docs.djangoproject.com/en/1.10/topics/db/models/#overriding-predefined-model-methods
    # Done: Having overwriten the  save method, ao all Action objects are created when the downtime is created

    def save(self, *args, **kwargs):

        if self.pk is None:
            super(Downtime, self).save(*args, **kwargs)
            characters = Character.objects.filter(domain=self.domain)
            for character in characters:
                Action(character=character, downtime=self).save()
        else:
            super(Downtime, self).save(*args, **kwargs)

    def __str__(self):
        return self.name + " " + str(self.start) + " - " + str(self.end)


class Action(models.Model):
    class Meta:
        verbose_name_plural = 'Actions'

    character = models.ForeignKey('Character', on_delete=models.CASCADE)
    downtime = models.ForeignKey('Downtime', on_delete=models.CASCADE)
    action = models.FileField(upload_to=set_upload_directory_path, blank=True, null=True)
    result = models.FileField(upload_to=set_upload_directory_path, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.character.firstname + " " + self.character.lastname + ": " + self.downtime.name

    @property
    def is_past_due(self):
        if date.today() > self.downtime.end:
            return True
        return False


class Secret(models.Model):
    class Meta:
        verbose_name_plural = 'Secrets'

    rank = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ]
    )
    clan = models.ForeignKey('Clan', on_delete=models.CASCADE)
    domain = models.ForeignKey('Domain', on_delete=models.CASCADE)
    description = models.TextField(null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description


class CharacterSecret(models.Model):
    class Meta:
        verbose_name_plural = 'Character secrets'

    character = models.ForeignKey('Character', on_delete=models.CASCADE)
    secret = models.ForeignKey('Secret', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.character.firstname + " " + self.character.lastname + ": " + self.secret.description


class BoonCategory(models.Model):
    class Meta:
        verbose_name_plural = 'Boon categories'

    name = models.CharField(max_length=200)
    weight = models.IntegerField(default=0)
    domain = models.ForeignKey('Domain')
    created = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + " " + str(self.weight)


class Boon(models.Model):
    # _ see: http://stackoverflow.com/questions/5893163/what-is-the-purpose-of-the-single-underscore-variable-in-python
    # could use it in future versions for a translations
    # STATUS = Choices(('draft', _('draft')), ('published', _('published')))
    STATUS = Choices((1, 'waiting', 'Waiting for approval'), (2, 'accepted', 'Accepted'), (3, 'declined', 'Declined'), (4, 'resolved', 'Resolved'))
    master = models.ForeignKey(Character, related_name='master', blank=True, null=True)
    slave = models.ForeignKey(Character, related_name='slave')
    category = models.ForeignKey(BoonCategory, related_name='category')
    note = models.TextField(default="please fill out a short decription")
    created = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)
    # GM
    approvedbygm = models.IntegerField(choices=STATUS, default=STATUS.waiting)
    approvedbygm_note = models.TextField(default="Place for additional notes")
    hash_gm = models.CharField(max_length=20, default="")
    # SLAVE
    approvedbyslave = models.IntegerField(choices=STATUS, default=STATUS.waiting)
    approvedbyslave_note = models.TextField(default="Place for additional notes")
    hash_slave = models.CharField(max_length=20, default="")
    # MASTER
    approvedbymaster = models.IntegerField(choices=STATUS, default=STATUS.waiting)
    approvedbymaster_note = models.TextField(default="Place for additional notes")
    hash_master = models.CharField(max_length=20, default="")

    def __str__(self):
        return self.slave.firstname + " " + self.slave.lastname + " owes a " + self.category.name + " to " + self.master.firstname + " " + self.master.lastname


class Xpearned(models.Model):
    class Meta:
        verbose_name_plural = 'XPs earned'

    characters = models.ManyToManyField(Character, blank=False)
    value = models.IntegerField(blank=False, null=False, default=1)
    event = models.ForeignKey(Event, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)
    note = models.CharField(max_length=250, blank=True, null=True)

    def displayCharacters(self):
        returnValue = ""
        first = True
        for character in self.characters.all():

            if first:
                returnValue += character.firstname + " " + character.lastname
                first = False
            else:
                returnValue += ", " + character.firstname + " " + character.lastname

        return returnValue

    def __str__(self):
        if self.event == None:
            return self.displayCharacters() + " earned " + str(self.value)
        else:
            return self.displayCharacters() + " earned " + str(self.value) + " at " + self.event.name


class Xpspent(models.Model):
    class Meta:
        verbose_name_plural = 'XPs spent'

    character = models.ForeignKey(Character, blank=False, default=1)
    oldvalue = models.IntegerField(blank=False, null=False, default=1)
    newvalue = models.IntegerField(blank=False, null=False, default=1)
    xpcost = models.IntegerField(blank=False, null=False, default=1)
    property = models.ForeignKey(Property, blank=False, default=1, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.character.firstname + " " + self.character.lastname + " spent " + str(self.xpcost) + " on " + self.property.name


class News(models.Model):
    class Meta:
        verbose_name_plural = 'News'

    caption = models.CharField(max_length=250, null=False)
    preface = HTMLField(default="Add an introduction here")
    content = HTMLField(default="Add the main content here")
    link = models.CharField(max_length=250, null=True, blank=True)
    validfrom = models.DateField(blank=True, null=True)
    validuntil = models.DateField(blank=True, null=True)
    domains = models.ManyToManyField(Domain)
    author = models.ForeignKey(Person)
    thumb = models.ImageField(upload_to=set_upload_directory_path, blank=True, null=True)
    image = models.ImageField(upload_to=set_upload_directory_path, blank=True, null=True)
    attachment = models.FileField(upload_to=set_upload_directory_path, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.caption + ": " + self.preface + "..."

    def displayDomains(self):
        returnValue = ""
        first = True
        for domain in self.domains.all():

            if first:
                returnValue += domain.name
                first = False
            else:
                returnValue += ", " + domain.name

        return returnValue


class Vision(models.Model):
    class Meta:
        verbose_name_plural = 'Visions'

    caption = models.CharField(max_length=250, null=False)
    preface = HTMLField(default="Add an introduction here")
    content = HTMLField(default="Add the main content here")
    domain = models.ForeignKey('Domain')
    author = models.ForeignKey(Person)
    attachment = models.FileField(upload_to=set_upload_directory_path, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)
    visionlevel = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ]
    )

    def __str__(self):
        return self.caption + ": " + self.preface + "..."


class SchreckNet(models.Model):
    class Meta:
        verbose_name_plural = 'SchreckNet messages'

    caption = models.CharField(max_length=250, null=False)
    preface = HTMLField(default="Add an introduction here")
    content = HTMLField(default="Add the main content here")
    domain = models.ForeignKey('Domain')
    author = models.ForeignKey(Person)
    attachment = models.FileField(upload_to=set_upload_directory_path, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)
    schrecknetlevel = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ]
    )

    def __str__(self):
        return self.caption + ": " + self.preface + "..."


################################ GENEALOGY ################################


class Genealogy(models.Model):
    class Meta:
        verbose_name_plural = 'Genealogy'

    name = models.CharField(max_length=100)
    sire = models.ForeignKey('Genealogy', blank=True, null=True)
    initial_generation = models.IntegerField(default=10, blank=True)
    current_generation = models.IntegerField(default=10, blank=True)
    character = models.ForeignKey('Character', blank=True, null=True)
    clan = models.ForeignKey('Clan', blank=True, null=True)
    domain = models.ForeignKey('Domain', default=1)
    created = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Name: " + self.name + ", Clan: " + str(
            self.clan) + ", initial generation: " + str(self.initial_generation) + ", current generation: " + str(
            self.current_generation) + ", Domain: " + str(self.domain)
