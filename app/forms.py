from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models
from django import forms

class IdeForm(forms.ModelForm):
    identifiant = forms.CharField(
        label=_('Identifiant'),
        widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off', 'placeholder': 'Entrez votre identifiant'}),
    )
    film = forms.CharField(
        label=_('Film ou série'),
        widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off', 'placeholder': 'Film ou série à ajouter'}),
    )

    class Meta:
        model = models.Ide
        fields = ("identifiant", "film")
        labels = {
            'identifiant': _('Identifiant'),
            'film': _('Film ou série'),
        }
