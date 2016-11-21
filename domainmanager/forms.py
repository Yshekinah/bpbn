from django import forms
from django.forms import ModelForm, Textarea, inlineformset_factory

from .models import *


class ActionForm(forms.ModelForm):
    class Meta:
        model = Action
        fields = ['action']


class CharacterFormCreate(forms.ModelForm):
    class Meta:
        model = Character
        exclude = ['clan_rank', 'humanity', 'frenzy', 'active', 'willpower', 'properties', 'bloodpool', 'schrecknetlevel', 'hasvisions', 'secretclan', 'finished', 'quickedit','levelup']


class CharacterFormEdit(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['firstname', 'lastname', 'nickname', 'image']


class BoonForm(ModelForm):
    class Meta:
        model = Boon
        fields = ['slave', 'category', 'note']


class CharacterShoppingForm(ModelForm):
    class Meta:
        model = CharacterShopping
        fields = ['property', 'mentor']


#CharacterPropertyFormSet = inlineformset_factory(Character, CharacterProperty, extra=0, can_delete=False, exclude=['property', 'timestamp'], widgets={'value': Textarea(attrs={'cols': 5, 'rows': 1})})
