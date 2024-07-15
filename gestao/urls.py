from django.urls import path
from gestao.views import loginview, index, registerview
app_name = 'gestao'

urlpatterns = [
    path('', index, name='index'),
    path('login/', loginview, name='login'),
    path('register/', registerview, name='register'),
]