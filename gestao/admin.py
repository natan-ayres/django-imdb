from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from gestao.models import Movies, ReviewsMovies, ReviewsSeries, News, Series, CustomUser, Groups

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'is_admin')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email','is_admin')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'is_admin')}
        ),
    )
    search_fields = ('username',)
    ordering = ('username',)

admin.site.register(CustomUser, CustomUserAdmin)

@admin.register(Groups)
class GroupsAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'date',
    ordering = '-id',
    search_fields = 'name', 'date', 'owner',
    list_per_page = 10
    list_editable = 'name',

@admin.register(Movies)
class MoviesAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'date'
    ordering = '-id',
    search_fields = 'name', 'date',
    list_per_page = 10
    list_editable = 'name','date',

@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'date',
    ordering = '-id',
    search_fields = 'name','date',
    list_per_page = 10
    list_editable = 'name','date',

@admin.register(ReviewsMovies)
class ReviewsMoviesAdmin(admin.ModelAdmin):
    list_display = 'id', 'user', 'movie', 'grade', 'show',
    ordering = '-id',
    search_fields = 'movie', 'grade', 'user'
    list_per_page = 10

@admin.register(ReviewsSeries)
class ReviewsSeriesAdmin(admin.ModelAdmin):
    list_display = 'id', 'user', 'serie', 'grade', 'show',
    ordering = '-id',
    search_fields = 'serie', 'grade', 'user'
    list_per_page = 10

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = 'id', 'name','date'
    ordering = '-id',
    search_fields = 'date', 'name'
    list_per_page = 5
