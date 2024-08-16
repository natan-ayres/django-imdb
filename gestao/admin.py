from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from gestao.models import Filmes, ReviewsFilmes, ReviewsSeries, Noticias, Series

@admin.register(Filmes)
class FilmesAdmin(admin.ModelAdmin):
    list_display = 'id', 'nome', 'data',
    ordering = '-id',
    search_fields = 'nome', 'data',
    list_per_page = 10
    list_editable = 'nome','data',

@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    list_display = 'id', 'nome', 'data',
    ordering = '-id',
    search_fields = 'nome','data',
    list_per_page = 10
    list_editable = 'nome','data',

@admin.register(ReviewsFilmes)
class ReviewsFilmesAdmin(admin.ModelAdmin):
    list_display = 'id', 'usuario', 'filme', 'nota',
    ordering = '-id',
    search_fields = 'filme', 'nota', 'usuario'
    list_per_page = 10

@admin.register(ReviewsSeries)
class ReviewsSeriesAdmin(admin.ModelAdmin):
    list_display = 'id', 'usuario', 'serie', 'nota',
    ordering = '-id',
    search_fields = 'serie', 'nota', 'usuario'
    list_per_page = 10

@admin.register(Noticias)
class NoticiasAdmin(admin.ModelAdmin):
    list_display = 'id', 'nome','data'
    ordering = '-id',
    search_fields = 'data', 'nome'
    list_per_page = 5