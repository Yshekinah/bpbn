from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.
from .models import *

admin.site.register(Country)
admin.site.register(Salutation)
admin.site.register(Gender)
admin.site.register(AgeCategory)
admin.site.register(PoliticalFuntion)
admin.site.register(Rank)
admin.site.register(Clan)
admin.site.register(Bloodline)
admin.site.register(Person)
admin.site.register(Domain)
admin.site.register(Character)
admin.site.register(BoonCategory)
admin.site.register(Boon)
admin.site.register(PropertyType)
admin.site.register(Property)
admin.site.register(CharacterProperty)
admin.site.register(Discipline)
admin.site.register(CharacterDiscipline)


# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class PersonInline(admin.StackedInline):
    model = Person
    can_delete = False
    verbose_name_plural = 'person'


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (PersonInline,)


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)


class VampireAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Vampire, VampireAdmin)
