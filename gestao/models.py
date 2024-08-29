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

class Groups(models.Model):
    class Meta:
        verbose_name = 'Group'
    
    name = models.CharField(max_length=30)
    image = models.ImageField(blank=True, upload_to='groups/')
    desc = models.TextField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True, related_name='owner')
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='members', blank=True)
    countmembers = models.IntegerField(default=0)
    waitlist = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='waitlist', blank=True)

    def __str__(self):
        return f'{self.name}' 

class Movies(models.Model):
    class Meta:
        verbose_name = 'Movie'


    CLASSIFICACOES_CHOICES = [
        ('Livre', 'Livre'),
        ('10', '10'),
        ('12', '12'),
        ('14', '14'),
        ('16', '16'),
        ('18', '18'),
    ]

    name = models.CharField(max_length=40)
    director = models.CharField(max_length=30, blank=True, null=True)
    writer = models.TextField(max_length=200, blank=True, null=True)
    actors = models.TextField(max_length=200, blank=True, null=True)
    runtime = models.TimeField(blank=True, null=True)
    rating = models.CharField(blank=True, null=True, max_length=20, choices=CLASSIFICACOES_CHOICES)
    plot = models.TextField(blank=True, null=True, max_length=400)
    date = models.DateField(null=True, blank=True)
    grade_avg = models.DecimalField(blank=True, null=True, max_digits=3, decimal_places=1)
    poster = models.ImageField(max_length=200, blank=True, null=True, upload_to= 'movies/')
    reviews = models.ManyToManyField(settings.AUTH_USER_MODEL, through='ReviewsMovies')

    def save(self, *args, **kwargs):
        if isinstance(self.runtime, str) and 'min' in self.runtime:
            minutes = int(self.runtime.split()[0])
            hours, minutes = divmod(minutes, 60)
            self.runtime = time(hour=hours, minute=minutes)
        if isinstance(self.date, str):
            self.date = datetime.strptime(self.date, '%d %b %Y').date()
        super().save(*args, **kwargs)

    def calc_avg(self):
        reviews = self.reviews.all() 
        if reviews.exists():
            avg = reviews.aggregate(Avg('grade'))['grade__avg']
            self.grade_avg = avg
        else:
            self.grade_avg = None

    def __str__(self):
        return f'{self.name}'
    
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
    
    poster = models.ImageField(max_length=200, blank=True, upload_to='series/')
    name = models.CharField(max_length=40)
    director = models.CharField(max_length=31, blank=True, null=True)
    writer = models.TextField(max_length=200, blank=True, null=True)
    actors = models.TextField(max_length=200, blank=True, null=True)
    rating = models.CharField(max_length=20, choices=CLASSIFICACOES_CHOICES)
    date = models.DateField(blank=True, null=True)
    date_end = models.DateField(blank=True, null=True)
    episodes = models.PositiveSmallIntegerField(blank=True, null=True)
    seasons = models.PositiveSmallIntegerField()
    plot = models.TextField(max_length=400)
    grade_avg = models.DecimalField(blank=True, null=True, max_digits=3, decimal_places=1)
    reviews = models.ManyToManyField(settings.AUTH_USER_MODEL, through='ReviewsSeries')

    def save(self, *args, **kwargs):
        if isinstance(self.date, str):
            self.date = datetime.strptime(self.date, '%d %b %Y').date()
        super().save(*args, **kwargs)

    def calc_avg(self):
        reviews = self.reviews.all() 
        if reviews.exists():
            avg = reviews.aggregate(Avg('grade'))['grade__avg']
            self.grade_avg = avg
        else:
            self.grade_avg = None

    def __str__(self):
        return f"{self.name} ({self.date.year})"
    
class News(models.Model):
    class Meta:
        verbose_name = 'News'

    name = models.CharField(max_length=31, validators=[MinLengthValidator(5)])
    image = models.ImageField(blank=True, upload_to='news/')
    text = models.TextField(max_length=684, validators=[MinLengthValidator(5)])
    date = models.DateTimeField(auto_now_add=True)
    show = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True,)

    def __str__(self):
        return f"{self.name} - {self.date.day}/{self.date.month}"


class ReviewsMovies(models.Model):
    class Meta:
        verbose_name = 'Review - Movie'

    movie = models.ForeignKey(Movies, related_name='reviewsmovie', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    review = models.TextField(max_length=250)
    grade = models.FloatField(validators=[MinValueValidator(0,0), MaxValueValidator(10,0)])
    show = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True,)

    def save(self, *args, **kwargs):
        super(ReviewsMovies, self).save(*args, **kwargs)
        self.movie.calc_avg()
        self.movie.save()

    def __str__(self):
        return f"Reviem from {self.movie.name} - Grade: {self.grade}"


class ReviewsSeries(models.Model):
    class Meta:
        verbose_name = 'Review - Serie'

    serie = models.ForeignKey(Series, related_name='reviewsserie', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    review = models.TextField(max_length=250)
    grade = models.FloatField(validators=[MinValueValidator(0,0), MaxValueValidator(10,0)])
    show = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True,)

    def save(self, *args, **kwargs):
        super(ReviewsSeries, self).save(*args, **kwargs)
        self.serie.calc_avg()
        self.serie.save()

    def __str__(self):
        return f"Reviem from {self.serie.name} - Grade: {self.grade}"
