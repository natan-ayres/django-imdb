from django.urls import path
from gestao.views import loginview, index, registerview, createfilme, createreview, createnoticia, createserie, listarfilmes, listarseries, infofilme, inforeview, infoserie
app_name = 'gestao'

urlpatterns = [
    path('', index, name='index'),
    
    path('login/', loginview, name='login'),
    path('register/', registerview, name='register'),

    path('criar/filme/', createfilme, name='criarfilme'),
    path('criar/review/', createreview, name='criarreview'),
    path('criar/noticia/', createnoticia, name='criarnoticia'),
    path('criar/serie/', createserie, name='criarserie'),

    path('filmes/', listarfilmes, name='listarfilmes'),
    path('series/', listarseries, name='listarseries'),

    path('filme/<int:filme_id>/', infofilme, name='infofilme'),
    path('review/<int:review_id>/', inforeview, name='inforeview'),
    path('serie/<int:serie_id>/', infoserie, name='infoserie')
]