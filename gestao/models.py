from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.db import models
from django.db.models import Avg
from django.contrib.auth.models import User

class Filmes(models.Model):
    nome = models.CharField(max_length=30)
    desc = models.TextField(max_length=100)
    data = models.DateField()
    foto = models.ImageField(blank=True, upload_to= 'posters/')
    nota_media = models.DecimalField(blank=True, null=True, max_digits=3, decimal_places=1)
    avaliacoes = models.ManyToManyField(User, through='Reviews')

    def calcular_nota_media(self):
        reviews = self.reviews.all()
        if reviews.exists():
            media = reviews.aggregate(Avg('nota'))['nota__avg']
            self.nota_media = media
        else:
            self.nota_media = None

    def save(self, *args, **kwargs):
        self.calcular_nota_media()
        super(Filmes, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.nome}'
