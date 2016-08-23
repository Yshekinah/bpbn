from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import *

admin.site.register(Country)
admin.site.register(Salutation)
admin.site.register(Gender)
admin.site.register(AgeCategory)
admin.site.register(PoliticalFuntion)
admin.site.register(Rank)
# admin.site.register(Clan)
# admin.site.register(Bloodline)
admin.site.register(Person)
# admin.site.register(Domain)
# admin.site.register(Character)
admin.site.register(BoonCategory)
admin.site.register(Boon)
# admin.site.register(PropertyType)
# admin.site.register(Property)
# admin.site.register(CharacterProperty)
# admin.site.register(Discipline)
# admin.site.register(CharacterDiscipline)
# admin.site.register(Event)
# admin.site.register(Xpearned)
# admin.site.register(Xpspent)
# admin.site.register(ClanProperty)
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


class PropertyAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    actions_selection_counter = True
    date_hierarchy = 'created'
    empty_value_display = '-empty-'
    list_display = ('name', 'get_type', 'initalizeatcharactercreation')
    list_filter = ('type', 'domain', 'initalizeatcharactercreation')

    # Show staff users only the properties they are allowed to edit
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


class XpearnedAdmin(admin.ModelAdmin):
    search_fields = ('character__firstname', 'character__lastname', 'event__caption', 'event__description', 'note',)
    actions_selection_counter = True
    date_hierarchy = 'created'
    empty_value_display = '-empty-'
    list_display = ('get_character', 'get_event', 'note', 'value', 'created')
    list_filter = ('character', 'event', 'value')

    # Show staff users only the properties they are allowed to edit
    def get_queryset(self, request):
        qs = super(XpearnedAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(character__domain=request.user.person.domain)

    def get_character(self, obj):
        return obj.character.firstname + obj.character.lastname

    get_character.short_description = 'Character'
    get_character.admin_order_field = 'character__lastname'

    def get_event(self, obj):
        if obj.event != None:
            return obj.event.caption

    get_event.short_description = 'Event'
    get_event.admin_order_field = 'event__caption'


class XpspentAdmin(admin.ModelAdmin):
    search_fields = ('character__firstname', 'character__lastname', 'property__name', 'property__type__name',)
    actions_selection_counter = True
    date_hierarchy = 'created'
    empty_value_display = '-empty-'
    list_display = ('get_character', 'get_property', 'oldvalue', 'newvalue', 'xpcost', 'created')
    list_filter = ('character', 'property', 'xpcost')

    # Show staff users only the properties they are allowed to edit
    def get_queryset(self, request):
        qs = super(XpspentAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(character__domain=request.user.person.domain)

    def get_character(self, obj):
        return obj.character.firstname + obj.character.lastname

    get_character.short_description = 'Character'
    get_character.admin_order_field = 'character__lastname'

    def get_property(self, obj):
        return obj.property.name

    get_property.short_description = 'Property'
    get_property.admin_order_field = 'property__name'


class EventAdmin(admin.ModelAdmin):
    search_fields = ('caption', 'description', 'domain__name')
    actions_selection_counter = True
    date_hierarchy = 'created'
    empty_value_display = '-empty-'
    list_display = ('caption', 'description', 'get_domain', 'start_date', 'end_date')
    list_filter = ('caption', 'description', 'domain', 'start_date', 'end_date')

    # Show staff users only the properties they are allowed to edit
    def get_queryset(self, request):
        qs = super(EventAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(domain=request.user.person.domain)

    def get_form(self, request, obj=None, **kwargs):
        form = super(EventAdmin, self).get_form(request, obj, **kwargs)
        # form class is created per request by modelform_factory function so it's safe to modify the the queryset
        if request.user.is_superuser:
            pass
        else:
            # get only the domain - the user is a member of
            form.base_fields['domain'].queryset = form.base_fields['domain'].queryset.filter(id=request.user.person.domain.id)
        return form

    def get_domain(self, obj):
        return obj.domain.name

    get_domain.short_description = 'Domain'
    get_domain.admin_order_field = 'domain__name'


class ClanAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    actions_selection_counter = True
    date_hierarchy = 'created'
    empty_value_display = '-empty-'
    list_display = ('name', 'parent', 'standardclan')
    list_filter = ('name', 'parent', 'standardclan')

    # Show staff users only the properties they are allowed to edit

    def get_queryset(self, request):
        qs = super(ClanAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(domain=request.user.person.domain)

    def get_form(self, request, obj=None, **kwargs):
        form = super(ClanAdmin, self).get_form(request, obj, **kwargs)
        # form class is created per request by modelform_factory function so it's safe to modify the the queryset
        if request.user.is_superuser:
            pass
        else:
            # get only the domain - the user is a member of
            form.base_fields['domain'].queryset = form.base_fields['domain'].queryset.filter(id=request.user.person.domain.id)
            form.base_fields['parent'].queryset = form.base_fields['parent'].queryset.filter(parent=None)
        return form


class DomainAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    actions_selection_counter = True
    date_hierarchy = 'created'
    empty_value_display = '-empty-'
    list_display = ('name', 'get_gm', 'get_substitute', 'street', 'postcode')
    list_filter = ('name', 'gm', 'substitute', 'street', 'postcode')

    # Show staff users only the properties they are allowed to edit

    def get_queryset(self, request):
        qs = super(DomainAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(id=request.user.person.domain.id)

    def get_form(self, request, obj=None, **kwargs):
        form = super(DomainAdmin, self).get_form(request, obj, **kwargs)
        # form class is created per request by modelform_factory function so it's safe to modify the the queryset
        if request.user.is_superuser:
            pass
        else:
            # get only the domain - the user is a member of
            form.base_fields['gm'].queryset = form.base_fields['gm'].queryset.filter(user__is_staff=1).filter(user__person__domain=request.user.person.domain)
            form.base_fields['substitute'].queryset = form.base_fields['substitute'].queryset.filter(user__is_staff=1).filter(user__person__domain=request.user.person.domain)
        return form

    def get_gm(self, obj):
        return obj.gm.user.first_name + " " + obj.gm.user.last_name

    get_gm.short_description = 'GM'

    def get_substitute(self, obj):
        return obj.substitute.user.first_name + " " + obj.substitute.user.last_name

    get_substitute.short_description = 'Substitute'


class ClanPropertyAdmin(admin.ModelAdmin):
    search_fields = ('property__name', 'clan__name')
    actions_selection_counter = True
    date_hierarchy = 'created'
    empty_value_display = '-empty-'
    list_display = ('get_property', 'get_clan')
    list_filter = ('property', 'clan')

    # Show staff users only the properties they are allowed to edit
    def get_queryset(self, request):
        qs = super(ClanPropertyAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(property__domain=request.user.person.domain)

    def get_form(self, request, obj=None, **kwargs):
        form = super(ClanPropertyAdmin, self).get_form(request, obj, **kwargs)
        # form class is created per request by modelform_factory function so it's safe to modify the the queryset
        if request.user.is_superuser:
            pass
        else:
            # get only the domain - the user is a member of
            form.base_fields['domain'].queryset = form.base_fields['domain'].queryset.filter(id=request.user.person.domain.id)
        return form

    def get_property(self, obj):
        return obj.property.name

    get_property.short_description = 'Disciplines'
    get_property.admin_order_field = 'property__name'

    def get_clan(self, obj):
        return obj.clan.name

    get_clan.short_description = 'Clan'
    get_clan.admin_order_field = 'clan__name'


admin.site.register(Character, CharacterAdmin)
admin.site.register(CharacterProperty, CharacterPropertyAdmin)
admin.site.register(Clan, ClanAdmin)
admin.site.register(ClanProperty, ClanPropertyAdmin)
admin.site.register(Domain, DomainAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Property, PropertyAdmin)
admin.site.register(PropertyType, PropertyTypeAdmin)
admin.site.register(Xpearned, XpearnedAdmin)
admin.site.register(Xpspent, XpspentAdmin)

admin.site.register(Vampire, VampireAdmin)
