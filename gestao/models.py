from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.db import models
from django.db.models import Avg
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator
from django.contrib.auth.models import User, AbstractUser
from django.conf import settings
from datetime import time, datetime

class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default=False) 

class Grupos(models.Model):
    class Meta:
        verbose_name = 'Grupo'
    
    nome = models.CharField(max_length=30)
    imagem = models.ImageField(blank=True, upload_to='grupos/')
    desc = models.TextField(max_length=200)
    data = models.DateTimeField(auto_now_add=True)
    dono = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True, related_name='dono')
    membros = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='membros', blank=True)
    waitlist = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='waitlist', blank=True)

    def __str__(self):
        return f'{self.nome}' 

class Filmes(models.Model):
    class Meta:
        verbose_name = 'Filme'


    CLASSIFICACOES_CHOICES = [
        ('Livre', 'Livre'),
        ('10', '10'),
        ('12', '12'),
        ('14', '14'),
        ('16', '16'),
        ('18', '18'),
    ]

    nome = models.CharField(max_length=30)
    diretor = models.CharField(max_length=30, blank=True, null=True)
    duracao = models.TimeField(blank=True, null=True)
    classificacao = models.CharField(blank=True, null=True, max_length=20, choices=CLASSIFICACOES_CHOICES)
    sinopse = models.TextField(blank=True, null=True, max_length=400)
    data = models.DateField(null=True, blank=True)
    nota_media = models.DecimalField(blank=True, null=True, max_digits=3, decimal_places=1)
    poster = models.ImageField(blank=True, null=True, upload_to= 'filmes/')
    avaliacoes = models.ManyToManyField(settings.AUTH_USER_MODEL, through='ReviewsFilmes')

    def save(self, *args, **kwargs):
        if isinstance(self.duracao, str) and 'min' in self.duracao:
            minutes = int(self.duracao.split()[0])
            hours, minutes = divmod(minutes, 60)
            self.duracao = time(hour=hours, minute=minutes)
        if isinstance(self.data, str):
            self.data = datetime.strptime(self.data, '%d %b %Y').date()
        super().save(*args, **kwargs)

    def calcular_nota_media(self):
        reviews = self.reviews.all() 
        if reviews.exists():
            media = reviews.aggregate(Avg('nota'))['nota__avg']
            self.nota_media = media
        else:
            self.nota_media = None

    def __str__(self):
        return f'{self.nome}'
    
class Series(models.Model):
    class Meta:
        verbose_name = 'Serie'

    CLASSIFICACOES_CHOICES = [
        ('Livre', 'Livre'),
        ('10', '10'),
        ('12', '12'),
        ('14', '14'),
        ('16', '16'),
        ('18', '18'),
    ]
    
    poster = models.ImageField(blank=True, upload_to='series/')
    nome = models.CharField(max_length=31)
    diretor = models.CharField(max_length=31, blank=True, null=True)
    classificacao = models.CharField(max_length=20, choices=CLASSIFICACOES_CHOICES)
    data = models.DateField(blank=True, null=True)
    data_termino = models.DateField(blank=True, null=True)
    episodios = models.PositiveSmallIntegerField()
    temporadas = models.PositiveSmallIntegerField()
    sinopse = models.TextField(max_length=400)
    nota_media = models.DecimalField(blank=True, null=True, max_digits=3, decimal_places=1)
    avaliacoes = models.ManyToManyField(settings.AUTH_USER_MODEL, through='ReviewsSeries')

    def calcular_nota_media(self):
        reviews = self.reviews.all() 
        if reviews.exists():
            media = reviews.aggregate(Avg('nota'))['nota__avg']
            self.nota_media = media
        else:
            self.nota_media = None

    def __str__(self):
        return f"{self.nome} ({self.data.year})"
    
class Noticias(models.Model):
    class Meta:
        verbose_name = 'Noticia'

    nome = models.CharField(max_length=31, validators=[MinLengthValidator(5)])
    imagem = models.ImageField(blank=True, upload_to='noticias/')
    texto = models.TextField(max_length=684, validators=[MinLengthValidator(5)])
    data = models.DateTimeField(auto_now_add=True)
    mostrar = models.BooleanField(default=False)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True,)

    def __str__(self):
        return f"{self.nome} - {self.data.day}/{self.data.month}"


class ReviewsFilmes(models.Model):
    class Meta:
        verbose_name = 'Review - Filme'

    filme = models.ForeignKey(Filmes, related_name='reviews', on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    review = models.TextField(max_length=250)
    nota = models.FloatField(validators=[MinValueValidator(0,0), MaxValueValidator(10,0)])
    mostrar = models.BooleanField(default=False)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True,)

    def save(self, *args, **kwargs):
        super(ReviewsFilmes, self).save(*args, **kwargs)
        self.filme.calcular_nota_media()
        self.filme.save()

    def __str__(self):
        return f"Avaliação de {self.filme.nome} - Nota: {self.nota}"


class ReviewsSeries(models.Model):
    class Meta:
        verbose_name = 'Review - Serie'

    serie = models.ForeignKey(Series, related_name='reviews', on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    review = models.TextField(max_length=250)
    nota = models.FloatField(validators=[MinValueValidator(0,0), MaxValueValidator(10,0)])
    mostrar = models.BooleanField(default=False)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True,)

    def save(self, *args, **kwargs):
        super(ReviewsSeries, self).save(*args, **kwargs)
        self.serie.calcular_nota_media()
        self.serie.save()

    def __str__(self):
        return f"Avaliação de {self.serie.nome} - Nota: {self.nota}"
