from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.db import models
from django.db.models import Avg
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

class Filmes(models.Model):
    nome = models.CharField(max_length=30)
    desc = models.TextField(max_length=100)
    data = models.DateField()
    foto = models.ImageField(blank=True, upload_to= 'images/')

    def __str__(self):
        return f'{self.nome}'
