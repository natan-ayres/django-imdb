from django.urls import path
from gestao.views import  index, loginview, registerview, logoutview, createfilme, createreviewfilme, createreviewserie, createnoticia, createserie, listarfilmes, listarseries, infofilme, infoserie, inforeviewfilme, inforeviewserie 
app_name = 'gestao'

urlpatterns = [
    path('', index, name='index'),
    
    path('login/', loginview, name='login'),
    path('register/', registerview, name='register'),
    path('logout/', logoutview, name='logout'),

    path('criar/filme/', createfilme, name='criarfilme'),
    path('criar/serie/', createserie, name='criarserie'),
    path('criar/noticia/', createnoticia, name='criarnoticia'),
    path('criar/review/filme/', createreviewfilme, name='criarreviewfilme'),
    path('criar/review/serie/', createreviewserie, name='criarreviewserie'),

    path('filmes/', listarfilmes, name='listarfilmes'),
    path('series/', listarseries, name='listarseries'),

    path('filme/<int:filme_id>/', infofilme, name='infofilme'),
    path('serie/<int:serie_id>/', infoserie, name='infoserie'),
    path('review/filme/<int:review_id>/', inforeviewfilme, name='inforeviewfilme'),
    path('review/serie/<int:review_id>/', inforeviewserie, name='inforeviewserie'),
]