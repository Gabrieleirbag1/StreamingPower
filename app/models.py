from django.db import models

class Ide(models.Model): 

    identifiant = models.CharField(max_length=10)
    film = models.CharField(max_length=30)
    
    def __str__(self):
        chaine = f"{self.identifiant} {self.film}"
        return chaine





# Create your models here.
