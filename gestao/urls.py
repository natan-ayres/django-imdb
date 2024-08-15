from django.urls import path
from gestao.views import  index, loginview, registerview, logoutview, createfilme, createreviewfilme, createreviewserie, createnoticia, createserie, updatefilme, updateserie, updatenoticia, listarfilmes, listarseries, infouser, infofilme, infoserie, inforeviewfilme, inforeviewserie
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

    path('update/filme/<int:filme_id>/', updatefilme, name='updatefilme'),
    path('update/serie/<int:serie_id>/', updateserie, name='updateserie'),
    path('update/noticia/<int:noticia_id>/', updatenoticia, name='updatenoticia'),
    

    path('filmes/', listarfilmes, name='listarfilmes'),
    path('series/', listarseries, name='listarseries'),

    path('user/<int:user_id>/', infouser, name='infouser'),
    path('filme/<int:filme_id>/', infofilme, name='infofilme'),
    path('serie/<int:serie_id>/', infoserie, name='infoserie'),
    path('review/filme/<int:review_id>/', inforeviewfilme, name='inforeviewfilme'),
    path('review/serie/<int:review_id>/', inforeviewserie, name='inforeviewserie'),


]