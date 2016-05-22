import datetime

from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

class Country(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=3)

    def __str__(self):
        return self.name

class Salutation(models.Model):
    name = models.CharField(max_length=100)

    STANDARD_SALUTATION = 1

    def __str__(self):
        return self.name

class Gender(models.Model):
    gender = models.CharField(max_length=1)

    def __str__(self):
        return self.gender

class AgeCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class PoliticalFuntion(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Rank(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Clan(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Bloodline(models.Model):
    name = models.CharField(max_length=100)
    parent_clan = models.ForeignKey(Clan,blank=True,)

    def __str__(self):
        return self.name + " descending from " + self.parent_clan.name

class Discipline(models.Model):
    name = models.CharField(max_length=100)
    clan = models.ForeignKey('Clan', related_name='clan')

    def __str__(self):
        return self.name

class Person(models.Model):
    salutation = models.ForeignKey(Salutation, default=Salutation.STANDARD_SALUTATION)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.EmailField()
    country = models.ForeignKey(Country)
    image = models.ImageField(blank=True)
    date_of_birth = models.DateField()
    description = models.TextField(blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.salutation.name + " " + self.firstname + " " + self.lastname + ", " + str(self.country)

class Domain(models.Model):
    name = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    postcode = models.CharField(max_length=10)
    country = models.ForeignKey(Country)
    gm = models.ForeignKey('Person', related_name='gm')
    substitute = models.ForeignKey('Person', related_name='substitute')

    def __str__(self):
        return self.name

class Character(models.Model):
    player = models.ForeignKey('Person',on_delete=models.CASCADE, default=1)
    salutation = models.ForeignKey(Salutation)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    generation = models.IntegerField(default=12)
    clan = models.ForeignKey(Clan)
    bloodline = models.ForeignKey(Bloodline)
    date_of_birth = models.DateField()
    date_of_death = models.DateField()
    gender = models.ForeignKey(Gender)
    rank = models.ForeignKey(Rank)
    clan_rank = models.IntegerField()
    function = models.ForeignKey(PoliticalFuntion, default=6)
    age_category = models.ForeignKey(AgeCategory)
    willpower = models.IntegerField()
    humanity = models.IntegerField()
    frenzy = models.IntegerField()
    bloodpool = models.IntegerField()
    active = models.BooleanField(default=True)
    sire = models.ForeignKey('Character', related_name='character_sire', blank=True, null=True)

    def __str__(self):
        return self.salutation.name + " " + self.firstname + " " + self.lastname

class PropertyType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Property(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey('PropertyType', related_name='type')

    def __str__(self):
        return self.name

class CharacterProperty(models.Model):
    character = models.ForeignKey('Character', related_name='cp_character')
    property = models.ForeignKey('Property', related_name='property')
    value = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
    )

    def __str__(self):
        return self.character.firstname + " " + self.character.lastname + ", " + self.property.name + ": " + str(self.value)

class CharacterDiscipline(models.Model):
    character = models.ForeignKey('Character', related_name='cd_character')
    discipline = models.ForeignKey('Discipline', related_name='discipline')
    level = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ]
    )

    def __str__(self):
        return self.character.firstname + " " + self.character.lastname + ", " + self.discipline.name + ": " + str(self.level)

class BoonCategory(models.Model):
    name = models.CharField(max_length=200)
    weight = models.IntegerField(default=0)

    def __str__(self):
        return self.name + " " + str(self.weight)


class Boon(models.Model):
    master = models.ForeignKey(Person, related_name='master')
    slave = models.ForeignKey(Person, related_name='slave')
    category = models.ForeignKey(BoonCategory, related_name='category')
    date = models.DateField(blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.slave.firstname + " " + self.slave.lastname + " owes a " + self.category.name + " to " + self.master.firstname + " " + self.master.lastname


################################ GENEALOGY ################################

class Vampire(models.Model):
    name = models.CharField(max_length=100)
    sire = models.ForeignKey('Vampire', related_name='master', blank=True, null=True)
    generation = models.IntegerField(default=10, blank=True)
    columnStart = models.IntegerField(default=0,blank=True)
    columnEnd = models.IntegerField(default=0,blank=True)

    def __str__(self):
        return self.name
