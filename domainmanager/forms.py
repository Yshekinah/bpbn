from django import forms
from django.forms import ModelForm, Textarea, inlineformset_factory

from .models import Boon, Character, CharacterProperty, CharacterShopping


class CharacterFormCreate(forms.ModelForm):
    class Meta:
        model = Character
        exclude = ['clan_rank', 'humanity', 'frenzy', 'active', 'willpower', 'properties']


class CharacterFormEdit(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['firstname', 'lastname', 'nickname']


class CharacterPropertiesForm(ModelForm):
    class Meta:
        model = CharacterProperty
        fields = ['property', 'value']


class BoonForm(ModelForm):
    class Meta:
        model = Boon
        fields = ['slave', 'category', 'note']


class CharacterShoppingForm(ModelForm):
    class Meta:
        model = CharacterShopping
        fields = ['property', 'newproperty', 'newpropertytype']
        # character = forms.ModelChoiceField(label='Character', queryset=Character.objects.all(), required=False)
        # property = forms.ModelChoiceField(label='Property', queryset=Property.objects.all(), required=False)
        # newproperty = forms.CharField(label="Your new property", required=False)
        # newpropertytype = forms.ModelChoiceField(label='Property type', queryset=PropertyType.objects.all(), required=False)


CharacterPropertyFormSet = inlineformset_factory(Character, CharacterProperty, extra=0, can_delete=False,
                                                 exclude=['property', 'timestamp'],
                                                 widgets={'value': Textarea(attrs={'cols': 5, 'rows': 1})})
