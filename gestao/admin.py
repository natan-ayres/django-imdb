from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from gestao.models import Filmes

@admin.register(Filmes)
class FilmesAdmin(admin.ModelAdmin):
    list_display = 'id', 'data',
    ordering = '-id',
    search_fields = 'data',
    list_per_page = 10
    list_editable = 'data',
