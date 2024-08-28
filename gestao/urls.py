from django.urls import path
from gestao.views import  index, loginview, registerview, logoutview, createfilme, createreviewfilme, createreviewserie, createnoticia, createserie, creategrupo,  updatefilme, updateserie, updatenoticia, updatereviewfilme, updatereviewserie, listarfilmes, listarseries, listargrupos, deletefilme, deleteserie,deletenoticia, deletereviewfilme, deletereviewserie, infouser, infofilme, infoserie, infonoticia, inforeviewfilme, inforeviewserie, update, deleteview, infogrupo, updategrupo, deletegrupo, adicionarwaitlist, adicionarmembro, negarwaitlist, apifilmes, apiseries
app_name = 'gestao'

urlpatterns = [
    path('', index, name='index'),

    path('api/filme/', apifilmes, name='apifilmes'),
    path('api/serie/', apiseries, name='apiseries'),
    
    path('login/', loginview, name='login'),
    path('register/', registerview, name='register'),
    path('logout/', logoutview, name='logout'),

    path('criar/filme/', createfilme, name='criarfilme'),
    path('criar/serie/', createserie, name='criarserie'),
    path('criar/noticia/', createnoticia, name='criarnoticia'),
    path('criar/review/filme/', createreviewfilme, name='criarreviewfilme'),
    path('criar/review/serie/', createreviewserie, name='criarreviewserie'),
    path('criar/grupo/',creategrupo, name='criargrupo'),

    path('delete/filme/<int:filme_id>/', deletefilme, name='deletefilme'),
    path('delete/serie/<int:serie_id>/', deleteserie, name='deleteserie'),
    path('delete/noticia/<int:noticia_id>/', deletenoticia, name='deletenoticia'),
    path('delete/review/filme/<int:review_id>/', deletereviewfilme, name='deletereviewfilme'),
    path('delete/review/serie/<int:review_id>/', deletereviewserie, name='deletereviewserie'),
    path('delete/grupo/<int:grupo_id>/', deletegrupo, name='deletegrupo'),
    path('delete/user/', deleteview, name='delete'),
    
    path('update/filme/<int:filme_id>/', updatefilme, name='updatefilme'),
    path('update/serie/<int:serie_id>/', updateserie, name='updateserie'),
    path('update/noticia/<int:noticia_id>/', updatenoticia, name='updatenoticia'),
    path('update/review/filme/<int:review_id>/', updatereviewfilme, name='updatereviewfilme'),
    path('update/review/serie/<int:review_id>/', updatereviewserie, name='updatereviewserie'),
    path('update/grupo/<int:grupo_id>/', updategrupo, name='updategrupo'),
    path('update/user/', update, name='update'),

    path('entrar/grupo/<int:grupo_id>/', adicionarwaitlist, name='adicionarwaitlist'),
    path('aceitar/<int:grupo_id>/<int:user_id>/', adicionarmembro, name='adicionarmembro'),
    path('negar/<int:grupo_id>/<int:user_id>/', negarwaitlist, name='negarwaitlist'),
    
    path('grupos/', listargrupos, name='listargrupos'),
    path('filmes/', listarfilmes, name='listarfilmes'),
    path('series/', listarseries, name='listarseries'),

    path('user/<int:user_id>/', infouser, name='infouser'),
    path('filme/<int:filme_id>/', infofilme, name='infofilme'),
    path('serie/<int:serie_id>/', infoserie, name='infoserie'),
    path('noticia/<int:noticia_id>/', infonoticia, name='infonoticia'),
    path('review/filme/<int:review_id>/', inforeviewfilme, name='inforeviewfilme'),
    path('review/serie/<int:review_id>/', inforeviewserie, name='inforeviewserie'),
    path('grupo/<int:grupo_id>/', infogrupo, name='infogrupo'),
    

]