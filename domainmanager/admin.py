from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import *

admin.site.register(Country)


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


class DowntimeAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    actions_selection_counter = True
    date_hierarchy = 'created'
    empty_value_display = '-empty-'
    list_display = ('name', 'get_event', 'start', 'end')
    list_filter = (('event', admin.RelatedOnlyFieldListFilter), 'start', 'end')

    # Show staff users only the properties they are allowed to edit
    def get_queryset(self, request):
        qs = super(DowntimeAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(domain=request.user.person.domain)

    def get_form(self, request, obj=None, **kwargs):
        form = super(DowntimeAdmin, self).get_form(request, obj, **kwargs)
        # form class is created per request by modelform_factory function so it's safe to modify the the queryset
        if request.user.is_superuser:
            pass
        else:
            # get only the domain - the user is a member of
            form.base_fields['domain'].queryset = form.base_fields['domain'].queryset.filter(id=request.user.person.domain.id)
        return form

    def get_event(self, obj):
        if obj.event:
            return obj.event.name

    get_event.short_description = 'Event'
    get_event.admin_order_field = 'event__name'


class ActionAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    actions_selection_counter = True
    date_hierarchy = 'created'
    empty_value_display = '-empty-'
    list_display = ('get_character', 'get_downtime', 'action', 'result')
    list_filter = (('downtime', admin.RelatedOnlyFieldListFilter), ('character', admin.RelatedOnlyFieldListFilter))

    # Show staff users only the properties they are allowed to edit
    def get_queryset(self, request):
        qs = super(ActionAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(character__domain=request.user.person.domain)

    def get_form(self, request, obj=None, **kwargs):
        form = super(ActionAdmin, self).get_form(request, obj, **kwargs)
        # form class is created per request by modelform_factory function so it's safe to modify the the queryset
        if request.user.is_superuser:
            pass
        else:
            # get only the domain - the user is a member of
            form.base_fields['character'].queryset = form.base_fields['character'].queryset.filter(domain=request.user.person.domain)
            form.base_fields['downtime'].queryset = form.base_fields['downtime'].queryset.filter(domain=request.user.person.domain)
        return form

    def get_character(self, obj):
        if obj.character:
            return obj.character.firstname + " " + obj.character.lastname

    get_character.short_description = 'Character'
    get_character.admin_order_field = 'character__lastname'

    def get_downtime(self, obj):
        if obj.downtime:
            return obj.downtime.name

    get_downtime.short_description = 'Downtime'
    get_downtime.admin_order_field = 'downtime__name'


class GenealogyAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    actions_selection_counter = True
    date_hierarchy = 'created'
    empty_value_display = '-empty-'
    list_display = ('name', 'current_generation', 'initial_generation', 'get_sire', 'get_clan')
    list_filter = (('clan', admin.RelatedOnlyFieldListFilter), 'current_generation', 'initial_generation')

    def get_clan(self, obj):
        if obj.clan:
            return obj.clan.name

    get_clan.short_description = 'Clan'
    get_clan.admin_order_field = 'clan__name'

    def get_sire(self, obj):
        if obj.sire:
            return obj.sire.name

    get_sire.short_description = 'Sire'
    get_sire.admin_order_field = 'sire__name'


class CharacterAdmin(admin.ModelAdmin):
    search_fields = ('firstname', 'lastname')
    actions_selection_counter = True
    date_hierarchy = 'created'
    empty_value_display = '-empty-'
    list_display = ('firstname', 'lastname', 'get_clan', 'generation', 'get_player')
    list_filter = (('clan', admin.RelatedOnlyFieldListFilter), 'generation', ('function', admin.RelatedOnlyFieldListFilter), 'humanity', 'hasvisions',
                   'schrecknetlevel', 'levelup', 'finished')

    # Show staff users only the properties they are allowed to edit
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


class CharacterCreationAdmin(admin.ModelAdmin):
    search_fields = ('character__firstname', 'character__lastname')
    actions_selection_counter = True
    date_hierarchy = 'created'
    empty_value_display = '-empty-'
    list_display = ('get_character', 'abilities', 'skills', 'disciplines', 'backgrounds', 'influences', 'secrets')
    list_filter = (('character', admin.RelatedOnlyFieldListFilter), 'abilities', 'skills', 'disciplines', 'backgrounds', 'influences', 'secrets')

    # Show staff users only the properties they are allowed to edit
    def get_queryset(self, request):
        qs = super(CharacterCreationAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(character__domain=request.user.person.domain)

    def get_form(self, request, obj=None, **kwargs):
        form = super(CharacterCreationAdmin, self).get_form(request, obj, **kwargs)
        # form class is created per request by modelform_factory function so it's safe to modify the the queryset
        if request.user.is_superuser:
            pass
        else:
            # get only the character - the character is a member of said domain
            form.base_fields['character'].queryset = form.base_fields['character'].queryset.filter(domain=request.user.person.domain)
        return form

    def get_character(self, obj):
        return obj.character.firstname + " " + obj.character.lastname

    get_character.short_description = 'Character'


class CharacterPropertyAdmin(admin.ModelAdmin):
    search_fields = ('property__name',)
    actions_selection_counter = True
    date_hierarchy = 'created'
    empty_value_display = '-empty-'
    list_display = ('get_property', 'value', 'get_character')
    list_filter = (('property', admin.RelatedOnlyFieldListFilter), 'value', ('character', admin.RelatedOnlyFieldListFilter))

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


class CharacterSecretAdmin(admin.ModelAdmin):
    search_fields = ('description',)
    actions_selection_counter = True
    date_hierarchy = 'created'
    empty_value_display = '-empty-'
    list_display = ('get_character', 'get_secret')
    list_filter = (('character', admin.RelatedOnlyFieldListFilter), ('secret', admin.RelatedOnlyFieldListFilter))

    # Show staff users only the properties they are allowed to edit
    def get_queryset(self, request):
        qs = super(CharacterSecretAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(secret__domain=request.user.person.domain)

    def get_form(self, request, obj=None, **kwargs):
        form = super(CharacterSecretAdmin, self).get_form(request, obj, **kwargs)
        # form class is created per request by modelform_factory function so it's safe to modify the the queryset
        if request.user.is_superuser:
            pass
        else:
            # get only the domain - the user is a member of
            # form.base_fields['domain'].queryset = form.base_fields['domain'].queryset.filter(id=request.user.person.domain.id)
            form.base_fields['character'].queryset = form.base_fields['character'].queryset.filter(domain=request.user.person.domain)
            form.base_fields['secret'].queryset = form.base_fields['secret'].queryset.filter(domain=request.user.person.domain)
            pass
        return form

    def get_character(self, obj):
        return obj.character.firstname + " " + obj.character.lastname

    get_character.short_description = 'Character'
    get_character.admin_order_field = 'character__lastname'

    def get_secret(self, obj):
        return obj.secret.description

    get_secret.short_description = 'Secret'
    get_secret.admin_order_field = 'secret__description'


class SecretAdmin(admin.ModelAdmin):
    search_fields = ('description',)
    actions_selection_counter = True
    date_hierarchy = 'created'
    empty_value_display = '-empty-'
    list_display = ('rank', 'get_clan', 'description')
    list_filter = ('rank', ('clan', admin.RelatedOnlyFieldListFilter))

    # Show staff users only the properties they are allowed to edit
    def get_queryset(self, request):
        qs = super(SecretAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(domain=request.user.person.domain)

    def get_form(self, request, obj=None, **kwargs):
        form = super(SecretAdmin, self).get_form(request, obj, **kwargs)
        # form class is created per request by modelform_factory function so it's safe to modify the the queryset
        if request.user.is_superuser:
            pass
        else:
            # get only the domain - the user is a member of
            form.base_fields['domain'].queryset = form.base_fields['domain'].queryset.filter(id=request.user.person.domain.id)
        return form

    def get_clan(self, obj):
        return obj.clan.name

    get_clan.short_description = 'Clan'
    get_clan.admin_order_field = 'clan__name'


class PropertyAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    actions_selection_counter = True
    date_hierarchy = 'created'
    empty_value_display = '-empty-'
    list_display = ('name', 'get_type', 'initalizeatcharactercreation', 'xpprize')
    list_filter = (('type', admin.RelatedOnlyFieldListFilter), ('domain', admin.RelatedOnlyFieldListFilter), 'initalizeatcharactercreation')

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
    list_filter = ('stattype', ('domain', admin.RelatedOnlyFieldListFilter), 'xpmultiplier', 'xpinitialprize')

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

    get_domain.short_description = 'Domain'
    get_domain.admin_order_field = 'domain__name'


class NewsAdmin(admin.ModelAdmin):
    search_fields = ('content',)
    actions_selection_counter = True
    date_hierarchy = 'created'
    empty_value_display = '-empty-'
    list_display = ('caption', 'content', 'displayDomains', 'validfrom', 'validuntil', 'isvision', 'schreknetlevel')
    list_filter = (
        'isvision', 'schreknetlevel', ('domains', admin.RelatedOnlyFieldListFilter), ('author', admin.RelatedOnlyFieldListFilter), 'validfrom',
        'validuntil')

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
    search_fields = ('event__name', 'event__description', 'note',)
    actions_selection_counter = True
    date_hierarchy = 'created'
    empty_value_display = '-empty-'
    list_display = ('get_event', 'displayCharacters', 'note', 'value', 'created')
    list_filter = (('characters', admin.RelatedOnlyFieldListFilter), ('event', admin.RelatedOnlyFieldListFilter), 'value')

    # Show staff users only the properties they are allowed to edit
    def get_queryset(self, request):
        qs = super(XpearnedAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(event__domain=request.user.person.domain)

    def get_form(self, request, obj=None, **kwargs):
        form = super(XpearnedAdmin, self).get_form(request, obj, **kwargs)
        # form class is created per request by modelform_factory function so it's safe to modify the the queryset
        if request.user.is_superuser:
            pass
        else:
            # get only the domain - the user is a member of
            form.base_fields['characters'].queryset = form.base_fields['characters'].queryset.filter(domain=request.user.person.domain)
        return form

    def get_event(self, obj):
        if obj.event != None:
            return obj.event.name

    get_event.short_description = 'Event'
    get_event.admin_order_field = 'event__name'


class XpspentAdmin(admin.ModelAdmin):
    search_fields = ('character__firstname', 'character__lastname', 'property__name', 'property__type__name',)
    actions_selection_counter = True
    date_hierarchy = 'created'
    empty_value_display = '-empty-'
    list_display = ('get_character', 'get_property', 'oldvalue', 'newvalue', 'xpcost', 'created')
    list_filter = (('character', admin.RelatedOnlyFieldListFilter), ('property', admin.RelatedOnlyFieldListFilter), 'xpcost')

    # Show staff users only the properties they are allowed to edit
    def get_queryset(self, request):
        qs = super(XpspentAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(character__domain=request.user.person.domain)

    def get_character(self, obj):
        return obj.character.firstname + " " + obj.character.lastname

    get_character.short_description = 'Character'
    get_character.admin_order_field = 'character__lastname'

    def get_property(self, obj):
        return obj.property.name

    get_property.short_description = 'Property'
    get_property.admin_order_field = 'property__name'


class EventAdmin(admin.ModelAdmin):
    search_fields = ('name', 'description', 'domain__name')
    actions_selection_counter = True
    date_hierarchy = 'created'
    empty_value_display = '-empty-'
    list_display = ('name', 'description', 'get_domain', 'start_date', 'end_date')
    list_filter = (('domain', admin.RelatedOnlyFieldListFilter),)

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
    list_display = ('name', 'standardclan')
    list_filter = ('standardclan',)

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
    search_fields = ('name', 'street', 'postcode')
    actions_selection_counter = True
    date_hierarchy = 'created'
    empty_value_display = '-empty-'
    list_display = (
    'name', 'get_gm', 'get_substitute', 'street', 'postcode', 'boons', 'secrets', 'downtimes', 'influences', 'advancedcharactercreation')
    list_filter = (('gm', admin.RelatedOnlyFieldListFilter), ('substitute', admin.RelatedOnlyFieldListFilter))

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
            form.base_fields['gm'].queryset = form.base_fields['gm'].queryset.filter(user__is_staff=1).filter(
                user__person__domain=request.user.person.domain)
            form.base_fields['substitute'].queryset = form.base_fields['substitute'].queryset.filter(user__is_staff=1).filter(
                user__person__domain=request.user.person.domain)
        return form

    def get_gm(self, obj):
        return obj.gm.user.first_name + " " + obj.gm.user.last_name

    get_gm.short_description = 'GM'

    def get_substitute(self, obj):
        return obj.substitute.user.first_name + " " + obj.substitute.user.last_name

    get_substitute.short_description = 'Substitute'


class AgeCategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    actions_selection_counter = True
    date_hierarchy = 'created'
    empty_value_display = '-empty-'
    list_display = ('name', 'startingxp', 'startingabilities', 'startingskills', 'startingdisciplines', 'startinginfluences', 'startingbackgrounds',
                    'startingsecrets')

    # list_filter = ('name', 'startingxp')

    # Show staff users only the properties they are allowed to edit
    def get_queryset(self, request):
        qs = super(AgeCategoryAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(domain=request.user.person.domain)

    def get_form(self, request, obj=None, **kwargs):
        form = super(AgeCategoryAdmin, self).get_form(request, obj, **kwargs)
        # form class is created per request by modelform_factory function so it's safe to modify the the queryset
        if request.user.is_superuser:
            pass
        else:
            # get only the domain - the user is a member of
            form.base_fields['domain'].queryset = form.base_fields['domain'].queryset.filter(pk=request.user.person.domain.id)
        return form


class PoliticalFuntionAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    actions_selection_counter = True
    date_hierarchy = 'created'
    empty_value_display = '-empty-'
    list_display = ('name', 'image')

    # Show staff users only the properties they are allowed to edit
    def get_queryset(self, request):
        qs = super(PoliticalFuntionAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(domain=request.user.person.domain)

    def get_form(self, request, obj=None, **kwargs):
        form = super(PoliticalFuntionAdmin, self).get_form(request, obj, **kwargs)
        # form class is created per request by modelform_factory function so it's safe to modify the the queryset
        if request.user.is_superuser:
            pass
        else:
            # get only the domain - the user is a member of
            form.base_fields['domain'].queryset = form.base_fields['domain'].queryset.filter(pk=request.user.person.domain.id)
        return form


class RankAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    actions_selection_counter = True
    date_hierarchy = 'created'
    empty_value_display = '-empty-'
    list_display = ('name', 'image')

    # Show staff users only the properties they are allowed to edit
    def get_queryset(self, request):
        qs = super(RankAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(domain=request.user.person.domain)

    def get_form(self, request, obj=None, **kwargs):
        form = super(RankAdmin, self).get_form(request, obj, **kwargs)
        # form class is created per request by modelform_factory function so it's safe to modify the the queryset
        if request.user.is_superuser:
            pass
        else:
            # get only the domain - the user is a member of
            form.base_fields['domain'].queryset = form.base_fields['domain'].queryset.filter(pk=request.user.person.domain.id)
        return form


class SectAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    actions_selection_counter = True
    date_hierarchy = 'created'
    empty_value_display = '-empty-'
    list_display = ('name', 'image')

    # Show staff users only the properties they are allowed to edit
    def get_queryset(self, request):
        qs = super(SectAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(domain=request.user.person.domain)

    def get_form(self, request, obj=None, **kwargs):
        form = super(SectAdmin, self).get_form(request, obj, **kwargs)
        # form class is created per request by modelform_factory function so it's safe to modify the the queryset
        if request.user.is_superuser:
            pass
        else:
            # get only the domain - the user is a member of
            form.base_fields['domain'].queryset = form.base_fields['domain'].queryset.filter(pk=request.user.person.domain.id)
        return form


class GenderAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    actions_selection_counter = True
    date_hierarchy = 'created'
    empty_value_display = '-empty-'
    list_display = ('name',)

    # Show staff users only the properties they are allowed to edit
    def get_queryset(self, request):
        qs = super(GenderAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(domain=request.user.person.domain)

    def get_form(self, request, obj=None, **kwargs):
        form = super(GenderAdmin, self).get_form(request, obj, **kwargs)
        # form class is created per request by modelform_factory function so it's safe to modify the the queryset
        if request.user.is_superuser:
            pass
        else:
            # get only the domain - the user is a member of
            form.base_fields['domain'].queryset = form.base_fields['domain'].queryset.filter(pk=request.user.person.domain.id)
        return form


class ClanPropertyAdmin(admin.ModelAdmin):
    search_fields = ('property__name', 'clan__name')
    actions_selection_counter = True
    date_hierarchy = 'created'
    empty_value_display = '-empty-'
    list_display = ('get_property', 'get_clan')
    list_filter = (('property', admin.RelatedOnlyFieldListFilter), ('clan', admin.RelatedOnlyFieldListFilter))

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


class CountryAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    actions_selection_counter = True
    date_hierarchy = 'created'
    empty_value_display = '-empty-'
    list_display = ('name',)
    list_filter = (('name', admin.RelatedOnlyFieldListFilter),)

    # Show staff users only the properties they are allowed to edit
    def get_queryset(self, request):
        qs = super(CountryAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(domain=request.user.person.domain)

    def get_form(self, request, obj=None, **kwargs):
        form = super(CountryAdmin, self).get_form(request, obj, **kwargs)
        # form class is created per request by modelform_factory function so it's safe to modify the the queryset
        if request.user.is_superuser:
            pass
        else:
            # get only the domain - the user is a member of
            form.base_fields['domain'].queryset = form.base_fields['domain'].queryset.filter(pk=request.user.person.domain.id)
        return form


class SalutationAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    actions_selection_counter = True
    date_hierarchy = 'created'
    empty_value_display = '-empty-'
    list_display = ('name',)

    # Show staff users only the properties they are allowed to edit
    def get_queryset(self, request):
        qs = super(SalutationAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(domain=request.user.person.domain)

    def get_form(self, request, obj=None, **kwargs):
        form = super(SalutationAdmin, self).get_form(request, obj, **kwargs)
        # form class is created per request by modelform_factory function so it's safe to modify the the queryset
        if request.user.is_superuser:
            pass
        else:
            # get only the domain - the user is a member of
            form.base_fields['domain'].queryset = form.base_fields['domain'].queryset.filter(pk=request.user.person.domain.id)
        return form


class BoonAdmin(admin.ModelAdmin):
    search_fields = ('master', 'slave', 'category')
    actions_selection_counter = True
    date_hierarchy = 'created'
    empty_value_display = '-empty-'
    list_display = ('get_master', 'get_slave', 'get_category', 'note')
    list_filter = (
        ('master', admin.RelatedOnlyFieldListFilter), ('slave', admin.RelatedOnlyFieldListFilter), ('category', admin.RelatedOnlyFieldListFilter),
        'approvedbygm', 'approvedbyslave', 'approvedbymaster')

    # Show staff users only the properties they are allowed to edit
    def get_queryset(self, request):
        qs = super(BoonAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(category__domain=request.user.person.domain)

    def get_form(self, request, obj=None, **kwargs):
        form = super(BoonAdmin, self).get_form(request, obj, **kwargs)
        # form class is created per request by modelform_factory function so it's safe to modify the the queryset
        if request.user.is_superuser:
            pass
        else:
            # get only the domain - the user is a member of
            form.base_fields['master'].queryset = form.base_fields['master'].queryset.filter(domain=request.user.person.domain)
            form.base_fields['category'].queryset = form.base_fields['category'].queryset.filter(domain=request.user.person.domain)
            form.base_fields['slave'].queryset = form.base_fields['slave'].queryset.filter(domain=request.user.person.domain)
        return form

    def get_master(self, obj):
        if obj.master != None:
            return obj.master.firstname + " " + obj.master.lastname

    get_master.short_description = 'Master'
    get_master.admin_order_field = 'master__lastname'

    def get_slave(self, obj):
        return obj.slave.firstname + " " + obj.slave.lastname

    get_slave.short_description = 'Slave'
    get_slave.admin_order_field = 'slave__lastname'

    def get_category(self, obj):
        return obj.category.name

    get_category.short_description = 'Boon category'
    get_category.admin_order_field = 'category__name'


class BoonCategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    actions_selection_counter = True
    date_hierarchy = 'created'
    empty_value_display = '-empty-'
    list_display = ('name', 'weight')

    # list_filter = ('name')

    # Show staff users only the properties they are allowed to edit
    def get_queryset(self, request):
        qs = super(BoonCategoryAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(domain=request.user.person.domain)

    def get_form(self, request, obj=None, **kwargs):
        form = super(BoonCategoryAdmin, self).get_form(request, obj, **kwargs)
        # form class is created per request by modelform_factory function so it's safe to modify the the queryset
        if request.user.is_superuser:
            pass
        else:
            # get only the domain - the user is a member of
            form.base_fields['domain'].queryset = form.base_fields['domain'].queryset.filter(pk=request.user.person.domain.id)
        return form


class CharacterShoppingAdmin(admin.ModelAdmin):
    # search_fields = ('character', 'property')
    actions_selection_counter = True
    date_hierarchy = 'created'
    empty_value_display = '-empty-'
    list_display = ('get_character', 'get_property', 'approvedbygm')
    list_filter = (('character', admin.RelatedOnlyFieldListFilter), ('property', admin.RelatedOnlyFieldListFilter),
                   'approvedbygm')

    # Show staff users only the properties they are allowed to edit
    def get_queryset(self, request):
        qs = super(CharacterShoppingAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(character__domain=request.user.person.domain)

    def get_form(self, request, obj=None, **kwargs):
        form = super(CharacterShoppingAdmin, self).get_form(request, obj, **kwargs)
        # form class is created per request by modelform_factory function so it's safe to modify the the queryset
        if request.user.is_superuser:
            pass
        else:
            # get only the domain - the user is a member of
            form.base_fields['character'].queryset = form.base_fields['character'].queryset.filter(domain=request.user.person.domain)
            form.base_fields['property'].queryset = form.base_fields['property'].queryset.filter(domain=request.user.person.domain)
        return form

    def get_character(self, obj):
        return obj.character.firstname + " " + obj.character.lastname

    get_character.short_description = 'Character'
    get_character.admin_order_field = 'character__lastname'

    def get_property(self, obj):
        if obj.property:
            return obj.property.name

    get_property.short_description = 'Property'
    get_property.admin_order_field = 'property__name'

    def get_newpropertytype(self, obj):
        if obj.newpropertytype:
            return obj.newpropertytype.name

    get_newpropertytype.short_description = 'Property type'
    get_newpropertytype.admin_order_field = 'newpropertytype__name'


class PersonAdmin(admin.ModelAdmin):
    search_fields = ('user__first_name', 'user__last_name', 'nickname')
    actions_selection_counter = True
    date_hierarchy = 'created'
    empty_value_display = '-empty-'
    list_display = ('get_firstname', 'get_lastname', 'nickname',)

    # Show staff users only the properties they are allowed to edit
    def get_queryset(self, request):
        qs = super(PersonAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(domain=request.user.person.domain)

    def get_form(self, request, obj=None, **kwargs):
        form = super(PersonAdmin, self).get_form(request, obj, **kwargs)
        # form class is created per request by modelform_factory function so it's safe to modify the the queryset
        if request.user.is_superuser:
            pass
        else:
            pass
        # get only the domain - the user is a member of
        form.base_fields['domain'].queryset = form.base_fields['domain'].queryset.filter(pk=request.user.person.domain.id)
        form.base_fields['user'].queryset = form.base_fields['user'].queryset.filter(person__domain=request.user.person.domain)
        form.base_fields['salutation'].queryset = form.base_fields['salutation'].queryset.filter(
            person__salutation__domain=request.user.person.domain)
        return form

    def get_firstname(self, obj):
        return obj.user.first_name

    get_firstname.short_description = 'Firstname'
    get_firstname.admin_order_field = 'user__first_name'

    def get_lastname(self, obj):
        return obj.user.last_name

    get_lastname.short_description = 'Lastname'
    get_lastname.admin_order_field = 'user__last_name'


admin.site.register(Action, ActionAdmin)
admin.site.register(AgeCategory, AgeCategoryAdmin)
admin.site.register(Boon, BoonAdmin)
admin.site.register(BoonCategory, BoonCategoryAdmin)
admin.site.register(Character, CharacterAdmin)
admin.site.register(CharacterCreation, CharacterCreationAdmin)
admin.site.register(CharacterProperty, CharacterPropertyAdmin)
admin.site.register(CharacterSecret, CharacterSecretAdmin)
admin.site.register(CharacterShopping, CharacterShoppingAdmin)
admin.site.register(Clan, ClanAdmin)
admin.site.register(ClanProperty, ClanPropertyAdmin)
admin.site.register(Domain, DomainAdmin)
admin.site.register(Downtime, DowntimeAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Gender, GenderAdmin)
admin.site.register(Genealogy, GenealogyAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(PoliticalFuntion, PoliticalFuntionAdmin)
admin.site.register(Property, PropertyAdmin)
admin.site.register(PropertyType, PropertyTypeAdmin)
admin.site.register(Rank, RankAdmin)
admin.site.register(Salutation, SalutationAdmin)
admin.site.register(Secret, SecretAdmin)
admin.site.register(Sect, SectAdmin)
admin.site.register(Xpearned, XpearnedAdmin)
admin.site.register(Xpspent, XpspentAdmin)
