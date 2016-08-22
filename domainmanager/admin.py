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
# admin.site.register(Character)
admin.site.register(BoonCategory)
admin.site.register(Boon)
# admin.site.register(PropertyType)
# admin.site.register(Property)
# admin.site.register(CharacterProperty)
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


class CharacterAdmin(admin.ModelAdmin):
    search_fields = ('firstname', 'lastname')
    actions_selection_counter = True
    date_hierarchy = 'created'
    empty_value_display = '-empty-'
    list_display = ('firstname', 'lastname', 'get_clan', 'generation', 'get_player')
    list_filter = ('clan', 'generation', 'function', 'humanity', 'hasvisions', 'schrecknetlevel')

    # Show staff users only the properteis they are allowed to edit
    def get_queryset(self, request):
        qs = super(CharacterAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(domain=request.user.person.domain)

    def get_form(self, request, obj=None, **kwargs):
        form = super(CharacterAdmin, self).get_form(request, obj, **kwargs)
        # form class is created per request by modelform_factory function so it's safe to modify the the queryset
        if request.user.is_superuser:
            pass
        else:
            # get only the domain - the user is a member of
            form.base_fields['domain'].queryset = form.base_fields['domain'].queryset.filter(id=request.user.person.domain.id)
        return form

    def get_player(self, obj):
        return obj.player.user.first_name + " " + obj.player.user.last_name

    get_player.short_description = 'Player'

    # get_player.admin_order_field = 'player__name'

    def get_clan(self, obj):
        return obj.clan.name

    get_clan.short_description = 'Clan'
    get_clan.admin_order_field = 'clan__name'

    def get_domain(self, obj):
        return obj.domain.name

    get_domain.short_description = 'Domain'
    get_domain.admin_order_field = 'domain__name'


admin.site.register(Character, CharacterAdmin)


class CharacterPropertyAdmin(admin.ModelAdmin):
    # search_fields = ('firstname', 'lastname')
    actions_selection_counter = True
    date_hierarchy = 'created'
    empty_value_display = '-empty-'
    list_display = ('get_property', 'value', 'get_character')
    list_filter = ('property', 'value', 'character')

    # Show staff users only the character properties they are allowed to edit
    def get_queryset(self, request):
        qs = super(CharacterPropertyAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(character__domain=request.user.person.domain)

    def get_form(self, request, obj=None, **kwargs):
        form = super(CharacterPropertyAdmin, self).get_form(request, obj, **kwargs)
        # form class is created per request by modelform_factory function so it's safe to modify the the queryset
        if request.user.is_superuser:
            pass
        else:
            pass
            # get only the domain - the user is a member of
            # form.base_fields['domain'].queryset = form.base_fields['domain'].queryset.filter(id=request.user.person.domain.id)
        return form

    def get_character(self, obj):
        return obj.character.firstname + " " + obj.character.lastname

    get_character.short_description = 'Character'

    # get_player.admin_order_field = 'player__name'

    def get_property(self, obj):
        return obj.property.name

    get_property.short_description = 'Property'
    get_property.admin_order_field = 'property__name'


admin.site.register(CharacterProperty, CharacterPropertyAdmin)


class PropertyAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    actions_selection_counter = True
    date_hierarchy = 'created'
    empty_value_display = '-empty-'
    list_display = ('name', 'get_type', 'initalizeatcharactercreation')
    list_filter = ('type', 'domain', 'initalizeatcharactercreation')

    # Show staff users only the properteis they are allowed to edit
    def get_queryset(self, request):
        qs = super(PropertyAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(domain=request.user.person.domain)

    def get_form(self, request, obj=None, **kwargs):
        form = super(PropertyAdmin, self).get_form(request, obj, **kwargs)
        # form class is created per request by modelform_factory function so it's safe to modify the the queryset
        if request.user.is_superuser:
            pass
        else:
            # get only the domain - the user is a member of
            form.base_fields['domain'].queryset = form.base_fields['domain'].queryset.filter(id=request.user.person.domain.id)
        return form

    def get_type(self, obj):
        return obj.type.name

    get_type.short_description = 'Property Type'
    get_type.admin_order_field = 'type__name'


admin.site.register(Property, PropertyAdmin)


class PropertyTypeAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    actions_selection_counter = True
    date_hierarchy = 'created'
    empty_value_display = '-empty-'
    list_display = ('name', 'stattype', 'get_domain', 'xpmultiplier', 'xpinitialprize')
    list_filter = ('name', 'stattype', 'domain', 'xpmultiplier', 'xpinitialprize')

    # Show staff users only the property types they are allowed to edit
    def get_queryset(self, request):
        qs = super(PropertyTypeAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(domain=request.user.person.domain)

    def get_form(self, request, obj=None, **kwargs):
        form = super(PropertyTypeAdmin, self).get_form(request, obj, **kwargs)
        # form class is created per request by modelform_factory function so it's safe to modify the the queryset
        if request.user.is_superuser:
            pass
        else:
            # give the user only the option to select the domain - the user is a member of
            form.base_fields['domain'].queryset = form.base_fields['domain'].queryset.filter(id=request.user.person.domain.id)
        return form

    def get_domain(self, obj):
        return obj.domain.name

    get_domain.short_description = 'Property Type'
    get_domain.admin_order_field = 'type__name'


admin.site.register(PropertyType, PropertyTypeAdmin)


class NewsAdmin(admin.ModelAdmin):
    search_fields = ('content',)
    actions_selection_counter = True
    date_hierarchy = 'created'
    empty_value_display = '-empty-'
    list_display = ('caption', 'content', 'displayDomains', 'validfrom', 'validuntil', 'isvision', 'schreknetlevel')
    list_filter = ('isvision', 'schreknetlevel', 'domains', 'author', 'validfrom', 'validuntil')

    fieldsets = (
        (None, {
            'fields': ('caption', 'preface', 'content', 'link', 'author', 'domains', 'validfrom', 'validuntil',)
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('schreknetlevel', 'limittoclan', 'isvision', 'image', 'thumb', 'attachment'),
        }),
    )

    # Let staff persons only select authors from their own domain who are staff themselves
    def get_form(self, request, obj=None, **kwargs):
        form = super(NewsAdmin, self).get_form(request, obj, **kwargs)
        # form class is created per request by modelform_factory function so it's safe to modify the the queryset
        if request.user.is_superuser:
            pass
        else:
            # give the user only the option to select the domain - the user is a member of
            form.base_fields['author'].queryset = form.base_fields['author'].queryset.filter(domain=request.user.person.domain).filter(
                user__is_staff=True)
        return form

    # def save_model(self, request, obj, form, change):
    # obj.author = request.user.person
    # obj.save()

    # Show staff users only the news they are allowed to edit
    def get_queryset(self, request):
        qs = super(NewsAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author__domain=request.user.person.domain)


admin.site.register(News, NewsAdmin)
