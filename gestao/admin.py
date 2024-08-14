from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from gestao.models import Filmes, Reviews, Noticias, Series

@admin.register(Filmes)
class FilmesAdmin(admin.ModelAdmin):
    list_display = 'id', 'nome', 'data',
    ordering = '-id',
    search_fields = 'nome', 'data',
    list_per_page = 10
    list_editable = 'nome','data',

@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    list_display = 'id', 'nome', 'data_lancamento',
    ordering = '-id',
    search_fields = 'nome','data_lancamento',
    list_per_page = 10
    list_editable = 'nome','data_lancamento',

@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = 'usuario', 'filme', 'nota',
    ordering = '-id',
    search_fields = 'filme', 'nota', 'usuario'
    list_per_page = 10

@admin.register(Noticias)
class NoticiasAdmin(admin.ModelAdmin):
    list_display = 'nome','data'
    ordering = '-id',
    search_fields = 'data', 'nome'
    list_per_page = 5