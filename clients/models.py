from django.db import models

class Client(models.Model):
    nom = models.CharField(max_length=255)
    adresse = models.TextField()
    telephone = models.CharField(max_length=20)
    email = models.EmailField(max_length=255, unique=True)
    date_naissance = models.DateField()
    numero_contrat = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.nom
