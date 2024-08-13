from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.db import models
from django.db.models import Avg
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator
from django.contrib.auth.models import User

class Filmes(models.Model):
    class Meta:
        verbose_name = 'Filme'

    OPCAO1 = 'opcao1'
    OPCAO2 = 'opcao2'
    OPCAO3 = 'opcao3'
    OPCAO4 = 'opcao4'
    OPCAO5 = 'opcao5'
    OPCAO6 = 'opcao6'

    CLASSIFICACOES_CHOICES = [
        (OPCAO1, 'Livre'),
        (OPCAO2, '10'),
        (OPCAO3, '12'),
        (OPCAO4, '14'),
        (OPCAO5, '16'),
        (OPCAO6, '18'),
    ]

    
    
    nome = models.CharField(max_length=30)
    diretor = models.CharField(max_length=30, blank=True, null=True)
    duracao = models.TimeField(blank=True, null=True)
    classificacao = models.CharField(max_length=20, choices=CLASSIFICACOES_CHOICES)
    desc = models.TextField(max_length=200)
    data = models.DateField()
    nota_media = models.DecimalField(blank=True, null=True, max_digits=3, decimal_places=1)
    poster = models.ImageField(blank=True, upload_to= 'posters/')
    avaliacoes = models.ManyToManyField(User, through='Reviews')

    def calcular_nota_media(self):
        reviews = self.reviews.all() 
        if reviews.exists():
            media = reviews.aggregate(Avg('nota'))['nota__avg']
            self.nota_media = media
        else:
            self.nota_media = None

    def __str__(self):
        return f'{self.nome} - {self.data.year}'
    
class Noticias(models.Model):
    class Meta:
        verbose_name = 'Noticia'

    nome = models.CharField(max_length=31, validators=[MinLengthValidator(5)])
    imagem = models.ImageField(blank=True, upload_to='noticias/')
    texto = models.TextField(max_length=684, validators=[MinLengthValidator(5)])
    data = models.DateTimeField(auto_now_add=True)
    mostrar = models.BooleanField(default=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True,)

    def __str__(self):
        return f"{self.nome} - {self.data.day}/{self.data.month}"


class Reviews(models.Model):
    class Meta:
        verbose_name = 'Review'

    filme = models.ForeignKey(Filmes, related_name='reviews', on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    review = models.TextField(max_length=250)
    nota = models.FloatField(validators=[MinValueValidator(0,0), MaxValueValidator(10,0)])
    show = models.BooleanField(default=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True,)

    def save(self, *args, **kwargs):
        super(Reviews, self).save(*args, **kwargs)
        self.filme.calcular_nota_media()
        self.filme.save()

    def __str__(self):
        return f"Avaliação de {self.filme.nome} - Nota: {self.nota}"

