from django import forms
from django.forms import inlineformset_factory, ModelForm, Textarea

from .models import Character, CharacterProperty



class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['firstname', 'lastname', 'generation', 'sire', 'clan', 'nickname']


class CharacterPropertiesForm(ModelForm):
    class Meta:
        model = CharacterProperty
        fields = ('property', 'value')


CharacterPropertyFormSet = inlineformset_factory(Character, CharacterProperty, can_delete=False, exclude=['property','timestamp'],
                                                 widgets={'value': Textarea(attrs={'cols': 5, 'rows': 1})})
