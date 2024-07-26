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
    nota_media = models.DecimalField(blank=True, null=True, max_digits=3, decimal_places=1)
    foto = models.ImageField(blank=True, upload_to= 'images/')
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
    
class Reviews(models.Model):
    filme = models.ForeignKey(Filmes, related_name='reviews', on_delete=models.CASCADE)
    review = models.TextField(max_length=250)
    nota = models.FloatField(validators=[MinValueValidator(0,0), MaxValueValidator(10,0)])
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True,)

    def save(self, *args, **kwargs):
        super(Reviews, self).save(*args, **kwargs)
        self.filme.calcular_nota_media()
        self.filme.save()

    def __str__(self):
        return f"Avaliação de {self.filme.nome} - Nota: {self.nota}"
    
@receiver(pre_save, sender=Reviews)
def set_contact_owner(sender, instance, **kwargs):
        if not instance.usuario_id:
            instance.usuario = instance._request_user

