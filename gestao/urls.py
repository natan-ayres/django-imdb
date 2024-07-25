from django.urls import path
from gestao.views import loginview, index, registerview, createfilme, createreview
app_name = 'gestao'

urlpatterns = [
    path('', index, name='index'),
    path('login/', loginview, name='login'),
    path('register/', registerview, name='register'),
    path('criar/filme/', createfilme, name='criar filme'),
    path('criar/review/', createreview, name='criar review')
]