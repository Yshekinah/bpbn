from django import template
from django.shortcuts import get_object_or_404

from domainmanager.models import Character, Person

register = template.Library()


# user in characterboonsummary.html to get the
# triplets in STATUS array for the approvals
@register.filter
def getValue(array, key):
    return array[int(key)]


# Tag for character selection
# calls characterSelection.html with queryset
# html renders the data
@register.inclusion_tag('characterSelection.html')
def characterSelection(id):
    player = get_object_or_404(Person, pk=id)
    characters = Character.objects.filter(player=player)
    return {'characters': characters}
