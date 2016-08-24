import random
import string
from datetime import date
from time import strftime

from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from model_utils import Choices


def set_upload_directory_path(instance, filename):
    ctype = ContentType.objects.get_for_model(instance)
    length = 4
    pool = string.ascii_letters + string.digits
    #    app = ctype.app_label
    extension = filename.split('.')[-1]
    name = filename.split('.')[0]

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
        return self.gender


class AgeCategory(models.Model):
    class Meta:
        verbose_name_plural = 'Age categories'

    name = models.CharField(max_length=100)
    startingxp = models.IntegerField(default=25)
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
    description = models.TextField(blank=True)
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
    caption = models.CharField(max_length=100, default="Insert event title")
    description = models.TextField()
    domain = models.ForeignKey(Domain)
    start_date = models.DateField()
    end_date = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.caption


class Property(models.Model):
    class Meta:
        verbose_name_plural = 'Properties'

    STATUS = Choices((1, 'yes', 'Yes'), (2, 'no', 'No'))
    name = models.CharField(max_length=100)
    type = models.ForeignKey('PropertyType', related_name='type')
    domain = models.ForeignKey(Domain, related_name='property_domain', default=1)
    initalizeatcharactercreation = models.IntegerField(choices=STATUS, default=STATUS.no, verbose_name="Initialize at character creation")
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


class Character(models.Model):
    class Meta:
        verbose_name_plural = 'Characters'

    STATUS = Choices((1, 'yes', 'Yes'), (2, 'no', 'No'), (3, 'active', 'Active'), (4, 'passive', 'Passive'))
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
            MaxValueValidator(20),
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
    active = models.IntegerField(choices=STATUS, default=STATUS.active)
    sire = models.ForeignKey('Character', related_name='character_sire', blank=True, null=True)
    hasvisions = models.IntegerField(choices=STATUS, default=STATUS.no, verbose_name="Visions", help_text="Has the character visions?")
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
                     (13, 'necromanticpaths', 'Necromantic Paths'))

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
    approvedbygm = models.IntegerField(choices=STATUS, default=STATUS.waiting)
    newproperty = models.CharField(max_length=50, blank=True, null=True)
    newpropertytype = models.ForeignKey(PropertyType, blank=True, null=True)
    hash_gm = models.CharField(max_length=20, default="")
    created = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        result = self.character.firstname + " " + self.character.lastname + " "
        if self.property:
            result += self.property.name + " "
        if self.newproperty:
            result += self.newproperty + " "
        if self.newpropertytype:
            result += self.newpropertytype.name
        return result


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

    character = models.ForeignKey(Character, blank=False, default=1)
    value = models.IntegerField(blank=False, null=False, default=1)
    event = models.ForeignKey(Event, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)
    note = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        if self.event == None:
            return self.character.firstname + " " + self.character.lastname + " earned " + str(self.value)
        else:
            return self.character.firstname + " " + self.character.lastname + " earned " + str(self.value) + " at " + self.event.caption


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
    preface = models.TextField(default="Add an introduction here")
    content = models.TextField(default="Add the main content here")
    link = models.CharField(max_length=250, null=True, blank=True)
    validfrom = models.DateField(blank=True, null=True)
    validuntil = models.DateField(blank=True, null=True)
    limittoclan = models.ManyToManyField(Clan, blank=True)
    domains = models.ManyToManyField(Domain)
    author = models.ForeignKey(Person)
    thumb = models.ImageField(upload_to=set_upload_directory_path, blank=True, null=True)
    image = models.ImageField(upload_to=set_upload_directory_path, blank=True, null=True)
    schreknetlevel = models.IntegerField(
        help_text='Does it require SchrekNet access?',
        default=0,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ]
    )
    attachment = models.FileField(upload_to=set_upload_directory_path, blank=True, null=True)
    isvision = models.BooleanField(default=False, help_text='Is it a vision?')
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


################################ GENEALOGY ################################


class Vampire(models.Model):
    name = models.CharField(max_length=100)
    sire = models.ForeignKey('Vampire', related_name='master', blank=True, null=True)
    generation = models.IntegerField(default=10, blank=True)
    columnStart = models.IntegerField(default=0, blank=True)
    columnEnd = models.IntegerField(default=0, blank=True)
    clan = models.ForeignKey('Clan', related_name='homeclan', blank=True, null=True)

    def __str__(self):
        return self.name
