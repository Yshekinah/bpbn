from django import forms
from django.forms import inlineformset_factory, ModelForm, Textarea

from .models import Character, CharacterProperty, Boon


class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['firstname', 'lastname', 'generation', 'sire', 'clan', 'nickname']


class CharacterFormCreate(forms.ModelForm):
    class Meta:
        model = Character
        exclude = ['clan_rank', 'humanity', 'frenzy', 'active', 'willpower', 'properties']
        data = {'firstname': 'Sepp'}


class CharacterPropertiesForm(ModelForm):
    class Meta:
        model = CharacterProperty
        fields = ['property', 'value']


class BoonForm(ModelForm):
    class Meta:
        model = Boon
        fields = ['slave', 'category', 'note']


CharacterPropertyFormSet = inlineformset_factory(Character, CharacterProperty, extra=0, can_delete=False,
                                                 exclude=['property', 'timestamp'],
                                                 widgets={'value': Textarea(attrs={'cols': 5, 'rows': 1})})
