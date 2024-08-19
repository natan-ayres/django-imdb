from django.urls import path
from gestao.views import  index, loginview, registerview, logoutview, createfilme, createreviewfilme, createreviewserie, createnoticia, createserie, updatefilme, updateserie, updatenoticia, updatereviewfilme, updatereviewserie, listarfilmes, listarseries, deletefilme, deleteserie,deletenoticia, deletereviewfilme, deletereviewserie, infouser, infofilme, infoserie, infonoticia, inforeviewfilme, inforeviewserie, update, deleteview
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

    path('delete/filme/<int:filme_id>/', deletefilme, name='deletefilme'),
    path('delete/serie/<int:serie_id>/', deleteserie, name='deleteserie'),
    path('delete/noticia/<int:noticia_id>/', deletenoticia, name='deletenoticia'),
    path('delete/review/filme/<int:review_id>/', deletereviewfilme, name='deletereviewfilme'),
    path('delete/review/serie/<int:review_id>/', deletereviewserie, name='deletereviewserie'),
    path('delete/user/', deleteview, name='delete'),
    
    path('update/filme/<int:filme_id>/', updatefilme, name='updatefilme'),
    path('update/serie/<int:serie_id>/', updateserie, name='updateserie'),
    path('update/noticia/<int:noticia_id>/', updatenoticia, name='updatenoticia'),
    path('update/review/filme/<int:review_id>/', updatereviewfilme, name='updatereviewfilme'),
    path('update/review/serie/<int:review_id>/', updatereviewserie, name='updatereviewserie'),
    path('update/user/<int:user_id>/', update, name='update'),
    

    path('filmes/', listarfilmes, name='listarfilmes'),
    path('series/', listarseries, name='listarseries'),

    path('user/<int:user_id>/', infouser, name='infouser'),
    path('filme/<int:filme_id>/', infofilme, name='infofilme'),
    path('serie/<int:serie_id>/', infoserie, name='infoserie'),
    path('noticia/<int:noticia_id>/', infonoticia, name='infonoticia'),
    path('review/filme/<int:review_id>/', inforeviewfilme, name='inforeviewfilme'),
    path('review/serie/<int:review_id>/', inforeviewserie, name='inforeviewserie'),


]