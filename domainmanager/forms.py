from django import forms

from .models import Character, CharacterProperty


class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        exclude = ['active']

class CharacterPropertyForm(forms.ModelForm):
    class Meta:
        model = CharacterProperty
        exclude = ['timestamp']
