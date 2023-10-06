from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models
from django import forms
from django.forms.widgets import ClearableFileInput

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



class ImgForm(forms.ModelForm):
    nom = forms.CharField(
        label=_('Nom'),
        widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off', 'placeholder': 'Entrez votre nom'}),
    )
    fichier = forms.ImageField(
        label=_('Image de profil'),
        widget=forms.FileInput(attrs={'class': 'form-control', 'autocomplete': 'off', 'placeholder': 'Modifier votre photo de profil'})
    )
    

    class Meta:
        model = models.Img
        fields = ['nom', 'fichier', 'imgid']
        labels = {
            'nom': _('Nom'),
            'fichier': _('Image de profil'),
            'imgid': _('ID utilisateur'),
        }
        
        
class InsForm(forms.ModelForm):

    pseudo = forms.CharField(
        label=_('Pseudo'),
        widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off', 'placeholder': 'Indiquez votre pseudo'}),
    )

    mdp = forms.CharField(
        label=_('Mdp'),
        widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off', 'type': "password", "placeholder": "Indiquez votre mot de passe"}),
    )

    verif_mdp = forms.CharField(
        label=_('Verif_mdp'),
        widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off', 'type': "password", 'placeholder': 'Confirmez votre mot de passe'}),
    )

    motif = forms.CharField(
        label=_('Motif'),
        widget=forms.Textarea(attrs={'class': 'form-control', 'autocomplete': 'off', 'placeholder': 'Expliquez pourquoi vous voulez obtenir un compte'}),
    )

    class Meta:
        model = models.Ins
        fields = ['pseudo', 'mdp', 'verif_mdp', 'motif']
        labels = {
            'pseudo': _('Pseudo'),
            'mdp': _('Mdp'),
            'verif_mdp': _('Verif_mdp'),
            'motif': _('Motif'),

        }
        

class SigForm(forms.ModelForm):
    
    probleme = forms.CharField(
        label=_('Probleme'),
        widget=forms.Select(attrs={'class': 'form-control', 'autocomplete': 'off'},choices=[('', 'Sélectionnez un problème')] + models.Sig.CHOICES),
    )

    media = forms.CharField(
        label=_('Media'),
        widget=forms.Select(attrs={'class': 'form-control', 'autocomplete': 'off'}, choices=[('', 'Sélectionnez un media')] + models.Sig.CHOICES2),
    )

    nom_media_ou_page = forms.CharField(
        label=_('Nom_media_ou_page'),
        widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off', 'placeholder': 'Indiquez le contenu concerné (media, page, etc.)'}),
    )

    description = forms.CharField(
        label=_('Description'),
        widget=forms.Textarea(attrs={'class': 'form-control', 'autocomplete': 'off', 'placeholder': "Ajoutez une description détaillée"}),
    )


    class Meta:
        model = models.Sig
        fields = ['probleme', 'media', 'nom_media_ou_page', 'description']
        labels = {
            'probleme': _('Probleme'),
            'media': _('Media'),
            'nom_media_ou_page': _('Nom_media_ou_page'),
            'description': _('Descripton'),
        }
        


