from django.shortcuts import render, redirect
from django.contrib import auth
from . forms import RegisterUpdateForm, RegisterForm, CustomAuthenticationForm, FilmesForm, ReviewForm

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

def registerview(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('gestao:login')


    return render(
        request,
        'register.html',
        {
            'form': form
        }
    )

def createfilme(request):
    form = FilmesForm()
    
    if request.method == 'POST':
        form = FilmesForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('gestao:index')
        
    return render(
        request,
        'registerfilme.html',
        {
            'form': form
        }
    )

def createreview(request):
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('gestao:index')
        
    return render(
        request,
        'registerreview.html',
        {
            'form': form
        }
    )