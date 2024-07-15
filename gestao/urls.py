from django.urls import path
from gestao.views import loginview, index
app_name = 'gestao'

urlpatterns = [
    path('', index, name='index'),
    path('login/', loginview, name='login'),
]