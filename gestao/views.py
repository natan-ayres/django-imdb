from django.shortcuts import render, redirect
from django.contrib import auth
from . forms import RegisterUpdateForm, RegisterForm, CustomAuthenticationForm

def index(request):
    context = {
        'site_title': 'Imdb-Django'
    }

    return render(
        request,
        'index.html',
        context
    )

def loginview(request):
    form = CustomAuthenticationForm(request)
    
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('gestao:index')
    
    return render(
        request,
        'login.html',
        {
            'form': form
        }
    )