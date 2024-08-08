from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import auth
from . models import Noticias
from . forms import RegisterUpdateForm, RegisterForm, CustomAuthenticationForm, FilmesForm, ReviewForm, NoticiasForm

def index(request):
    try:

        noticias = Noticias.objects \
            .filter(mostrar = True) \
            .order_by('-data') \
            .distinct() 

        context = {
            'noticias': noticias,
            'site_title': 'Imdb-Django'
        }

        return render(
            request,
            'index.html',
            context
        )
    
    except AttributeError:
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
        form = FilmesForm(request.POST, request.FILES)

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
    form = ReviewForm(usuario=request.user)

    if request.method == 'POST':
        form = ReviewForm(request.POST, usuario=request.user)

        if form.is_valid():
            review = form.save(commit=False)
            review.usuario = request.user
            review.save()
            return redirect('gestao:index')
        
    return render(
        request,
        'registerreview.html',
        {
            'form': form
        }
    )

def createnoticia(request):
    form = NoticiasForm()

    if request.method == 'POST':
        form = NoticiasForm(request.POST,  request.FILES)

        if form.is_valid():
            noticia = form.save(commit=False)
            noticia.usuario = request.user
            noticia.save()
            return redirect('gestao:index')
        
    
    return render(
        request,
        'registernoticia.html',
        {
            'form': form,
            'site_title': 'Criar Noticias'
        }
    )


