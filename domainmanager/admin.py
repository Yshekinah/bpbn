from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import *

admin.site.register(Country)
admin.site.register(Salutation)
admin.site.register(Gender)
admin.site.register(AgeCategory)
admin.site.register(PoliticalFuntion)
admin.site.register(Rank)
admin.site.register(Clan)
# admin.site.register(Bloodline)
admin.site.register(Person)
admin.site.register(Domain)
admin.site.register(Character)
admin.site.register(BoonCategory)
admin.site.register(Boon)
admin.site.register(PropertyType)
admin.site.register(Property)
admin.site.register(CharacterProperty)
# admin.site.register(Discipline)
# admin.site.register(CharacterDiscipline)
admin.site.register(Event)
admin.site.register(Xpearned)
admin.site.register(Xpspent)
admin.site.register(ClanProperty)
admin.site.register(CharacterShopping)
# admin.site.register(News)
admin.site.register(Sect)


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


class NewsAdmin(admin.ModelAdmin):
    search_fields = ('content',)
    verbose_name_plural = 'News'
    actions_selection_counter = True
    date_hierarchy = 'created'
    empty_value_display = '-empty-'
    list_display = ('caption', 'content', 'displayDomains', 'validfrom', 'validuntil', 'isvision', 'schreknetlevel')
    list_filter = ('isvision', 'schreknetlevel', 'domains', 'author', 'validfrom', 'validuntil')

    fieldsets = (
        (None, {
            'fields': ('caption', 'preface', 'content', 'link', 'domains', 'validfrom', 'validuntil',)
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('schreknetlevel', 'limittoclan', 'isvision', 'image', 'thumb', 'attachment'),
        }),
    )

    def save_model(self, request, obj, form, change):
        obj.author = request.user.person
        obj.save()

    def get_queryset(self, request):
        qs = super(NewsAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author__domain=request.user.person.domain)


admin.site.register(News, NewsAdmin)
