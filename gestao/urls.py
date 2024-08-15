from django.urls import path
from gestao.views import loginview, index, registerview, createfilme, createreviewfilme, createreviewserie, createnoticia, createserie, listarfilmes, listarseries, infofilme, inforeviewfilme, infoserie, logoutview
app_name = 'gestao'

urlpatterns = [
    path('', index, name='index'),
    
    path('login/', loginview, name='login'),
    path('register/', registerview, name='register'),
    path('logout/', logoutview, name='logout'),

    path('criar/filme/', createfilme, name='criarfilme'),
    path('criar/review/filme/', createreviewfilme, name='criarreviewfilme'),
    path('criar/review/serie/', createreviewserie, name='criarreviewserie'),
    path('criar/noticia/', createnoticia, name='criarnoticia'),
    path('criar/serie/', createserie, name='criarserie'),

    path('filmes/', listarfilmes, name='listarfilmes'),
    path('series/', listarseries, name='listarseries'),

    path('filme/<int:filme_id>/', infofilme, name='infofilme'),
    path('review/<int:review_id>/', inforeviewfilme, name='inforeview'),
    path('serie/<int:serie_id>/', infoserie, name='infoserie')
]