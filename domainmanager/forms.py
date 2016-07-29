from django import forms
from django.forms import ModelForm, Textarea, inlineformset_factory

from .models import Boon, Character, CharacterProperty, Property, PropertyType


class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['firstname', 'lastname', 'generation', 'sire', 'clan', 'nickname']


class CharacterFormCreate(forms.ModelForm):
    class Meta:
        model = Character
        exclude = ['clan_rank', 'humanity', 'frenzy', 'active', 'willpower', 'properties']


class CharacterPropertiesForm(ModelForm):
    class Meta:
        model = CharacterProperty
        fields = ['property', 'value']


class BoonForm(ModelForm):
    class Meta:
        model = Boon
        fields = ['slave', 'category', 'note']


class CharacterShoppingForm(forms.Form):
    #    class Meta:
    # model = CharacterShopping
    character = forms.ModelChoiceField(label='Character', queryset=Character.objects.all(), required=False)
    property = forms.ModelChoiceField(label='Property', queryset=Property.objects.all(), required=False)
    newproperty = forms.CharField(label="Your new property", required=False)
    newpropertytype = forms.ModelChoiceField(label='Property type', queryset=PropertyType.objects.all(), required=False)
    fields = ['property', 'newproperty', 'newpropertytype']


CharacterPropertyFormSet = inlineformset_factory(Character, CharacterProperty, extra=0, can_delete=False,
                                                 exclude=['property', 'timestamp'],
                                                 widgets={'value': Textarea(attrs={'cols': 5, 'rows': 1})})
