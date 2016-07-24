from django import forms
from django.forms import inlineformset_factory

from .models import Character, CharacterProperty


class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        exclude = ['active', 'properties']

CharacterPropertyFormSet = inlineformset_factory(Character, CharacterProperty, can_delete=False, exclude = ['id'])
