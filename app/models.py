from django.db import models
from django.contrib.auth.models import User 


class Ide(models.Model): 

    identifiant = models.CharField(max_length=10)
    film = models.CharField(max_length=30)
    
    def __str__(self):
        chaine = f"{self.identifiant} {self.film}"
        return chaine


class Img(models.Model):
    nom = models.CharField(max_length=255)
    fichier = models.ImageField(upload_to='propterre/media/propterre', default=None)
    imgid = models.ForeignKey(User, on_delete=models.CASCADE, default=None)


class Ins(models.Model):
    pseudo = models.CharField(max_length=255)
    mdp = models.CharField(max_length=255)
    verif_mdp = models.CharField(max_length=255)
    motif = models.CharField(max_length=1000)
    

class Sig(models.Model):
    CHOICES = [
        ("Problème de lecture audio", [
            ("pas_de_son", "Pas de son"),
            ("qualite_son", "La qualité du son n'est pas bonne"),
        ]),
        ("Problème de lecture vidéo", [
            ("pas_de_video", "Pas d'image"),
            ("video_sacadee", "La lecture de l'image est saccadée"),
            ("qualite_video", "La qualité de l'image n'est pas bonne"),
        ]),
        ("Problème du lecteur", [
            ("elements_lecteur", "Des éléments du lecteur vidéo ne fonctionnent pas correctement"),
            ("sous_titres_affichage", "Les sous-titres ne s'affichent pas correctement (visuellement)"),
            ("pas_de_sous_titres", "Les sous-titres ne fonctionnent pas"),
            ("sous_titres_synchronisation", "Les sous-titres ne sont pas synchronisés avec l'image"),
        ]),
        ("Problème d'interface", [
            ("interface_affichage", "La page ne s'affiche pas correctement"),
            ("interface_chargement", "La page ne charge pas ou trop lentement"),
            ("interface_elements", "Des éléments de la page ne fonctionnent pas correctement (boutons, formulaire, etc.)"),
            ("interface_acces", "La page est inaccessible"),
            ("modification_profil", "La modification de la photo de profil ne fonctionne pas correctement"),
            ("affichage_profil", "La photo de profil ne s'affiche plus"),
        ]),
    ]

    CHOICES2 = [
        ("Media", [
        ("film", "Film"),
        ("serie", "Série"),
        ]),
        ("Interface", [
            ("all", "Toutes les pages"),
            ("home", "Page d'accueil"),
            ("films", "Page de lecture de films"),
            ("series", "Page de lecture de séries"),
            ("profil", "Page de profil"),
        ]),
    ]

    probleme = models.CharField(max_length=255, choices=CHOICES)
    media = models.CharField(max_length=255, choices=CHOICES2)
    nom_media_ou_page = models.CharField(max_length=255)
    description = models.CharField(max_length=2000, default=None, null=True, blank=True)







# Create your models here.
