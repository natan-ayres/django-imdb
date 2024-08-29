from django.urls import path
from gestao.views import  index, loginview, registerview, logoutview, createmovie, createreviewmovie, createreviewserie, createnews, createserie, creategroup,  updatemovie, updateserie, updatenews, updatereviewmovie, updatereviewserie, listmovies, listseries, listgroups, deletemovie, deleteserie,deletenews, deletereviewmovie, deletereviewserie, infouser, infomovie, infoserie, infonews, inforeviewmovie, inforeviewserie, update, deleteview, infogroup, updategroup, deletegroup, addwaitlist, addmember, negarwaitlist, apimovies, apiseries, infomembers, removemember, infomoviegroup, infoseriegroup
app_name = 'gestao'

urlpatterns = [
    path('', index, name='index'),

    path('api/movie/', apimovies, name='apimovies'),
    path('api/serie/', apiseries, name='apiseries'),
    
    path('login/', loginview, name='login'),
    path('register/', registerview, name='register'),
    path('logout/', logoutview, name='logout'),

    path('create/movie/', createmovie, name='createmovie'),
    path('create/serie/', createserie, name='createserie'),
    path('create/news/', createnews, name='createnews'),
    path('create/review/movie/', createreviewmovie, name='createreviewmovie'),
    path('create/review/serie/', createreviewserie, name='createreviewserie'),
    path('create/group/',creategroup, name='creategroup'),

    path('delete/movie/<int:movie_id>/', deletemovie, name='deletemovie'),
    path('delete/serie/<int:serie_id>/', deleteserie, name='deleteserie'),
    path('delete/news/<int:news_id>/', deletenews, name='deletenews'),
    path('delete/review/movie/<int:review_id>/', deletereviewmovie, name='deletereviewmovie'),
    path('delete/review/serie/<int:review_id>/', deletereviewserie, name='deletereviewserie'),
    path('delete/group/<int:group_id>/', deletegroup, name='deletegroup'),
    path('delete/user/', deleteview, name='delete'),
    
    path('update/movie/<int:movie_id>/', updatemovie, name='updatemovie'),
    path('update/serie/<int:serie_id>/', updateserie, name='updateserie'),
    path('update/news/<int:news_id>/', updatenews, name='updatenews'),
    path('update/review/movie/<int:review_id>/', updatereviewmovie, name='updatereviewmovie'),
    path('update/review/serie/<int:review_id>/', updatereviewserie, name='updatereviewserie'),
    path('update/group/<int:group_id>/', updategroup, name='updategroup'),
    path('update/user/', update, name='update'),

    path('join/group/<int:group_id>/', addwaitlist, name='addwaitlist'),
    path('accept/<int:group_id>/<int:user_id>/', addmember, name='addmember'),
    path('reject/<int:group_id>/<int:user_id>/', negarwaitlist, name='negarwaitlist'),
    path('leave/<int:group_id>/<int:user_id>/', removemember, name='removemember'),
    
    path('groups/', listgroups, name='listgroups'),
    path('movies/', listmovies, name='listmovies'),
    path('series/', listseries, name='listseries'),

    path('user/<int:user_id>/', infouser, name='infouser'),
    path('movie/<int:movie_id>/', infomovie, name='infomovie'),
    path('serie/<int:serie_id>/', infoserie, name='infoserie'),
    path('news/<int:news_id>/', infonews, name='infonews'),
    path('review/movie/<int:review_id>/', inforeviewmovie, name='inforeviewmovie'),
    path('review/serie/<int:review_id>/', inforeviewserie, name='inforeviewserie'),
    path('group/<int:group_id>/', infogroup, name='infogroup'),
    path('group/<int:group_id>/members/', infomembers, name='infomembers'),
    path('movie/<int:movie_id>/<int:group_id>/', infomoviegroup, name='infomoviegroup'),
    path('serie/<int:serie_id>/<int:group_id>/', infoseriegroup, name='infoseriegroup'),

]