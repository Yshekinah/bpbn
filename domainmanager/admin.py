from django.contrib import admin

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
admin.site.register(Vampire)
admin.site.register(BoonCategory)
admin.site.register(Boon)

