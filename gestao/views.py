from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.urls import reverse
from django.contrib import auth
from . models import Noticias, Filmes, Reviews
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
            return redirect('gestao:listarfilmes')
        
    return render(
        request,
        'registermodel.html',
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
        'registermodel.html',
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
        'registermodel.html',
        {
            'form': form,
            'site_title': 'Criar Noticias'
        }
    )

def infofilme(request, filme_id):
    try:
        single_filme = Filmes.objects.get(pk=filme_id)
    except Filmes.DoesNotExist:
        return redirect('gestao:index')
    
    reviews = Reviews.objects \
        .filter(show=True, filme_id = single_filme)\
        .order_by('-id')

    paginator = Paginator(reviews, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

        
    site_title = f'{single_filme.nome} - {single_filme.data.year}'

    context = {
        'review': reviews,
        'page_obj': page_obj,
        'filme': single_filme,
        'site_title': site_title
    }

    return render(
        request,
        'filmeinfo.html',
        context
    )


def listarfilmes(request):
    try:

        filmes = Filmes.objects \
            .order_by('-id') \
            .distinct() 

        paginator = Paginator(filmes, 6)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        context = {
            'filmes': filmes,
            'page_obj': page_obj,
            'site_title': 'Filmes'
        }

        return render(
            request,
            'filmes.html',
            context
        )
    
    except AttributeError:
        context = {
            'site_title': 'Filmes'
        }

        return render(
            request,
            'filmes.html',
            context
        )
    
def inforeview(request, review_id):
    try:
        single_review = Reviews.objects.get(pk=review_id)
    except Reviews.DoesNotExist:
        return redirect('gestao:index')
    
    site_title = f'{single_review.usuario} - {single_review.nota}'

    context = {
        'review': single_review,
        'site_title': site_title
    }

    return render(
        request,
        'reviewinfo.html',
        context
    )