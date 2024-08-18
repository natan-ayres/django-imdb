from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.urls import reverse
from django.contrib import auth
from . models import Noticias, Filmes, ReviewsFilmes, ReviewsSeries, Series, CustomUser
from . forms import RegisterUpdateForm, RegisterForm, CustomAuthenticationForm, FilmesForm, ReviewFilmeForm, ReviewUpdateFilmeForm, ReviewSeriesForm, ReviewUpdateSeriesForm, NoticiasForm, SeriesForm

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
            'countertext': 'Não possui conta? Cadastre-se aqui',
            'counterlink': 'gestao:register',
            'botao': 'Entrar',
            'site_title': 'Login',
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
        'login.html',
        {
            'countertext': 'Já possui conta? Entre por aqui',
            'counterlink': 'gestao:login',
            'botao': 'Cadastre-se',
            'site_title': 'Cadastro',
            'form': form
        }
    )

def logoutview(request):
    auth.logout(request)
    return redirect('gestao:login')

def createfilme(request):
    form = FilmesForm()
    
    if request.method == 'POST':
        form = FilmesForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('gestao:listarfilmes')
        
    return render(
        request,
        'register.html',
        {
            'form': form
        }
    )

def createreviewfilme(request):
    form = ReviewFilmeForm(usuario=request.user)

    if request.method == 'POST':
        form = ReviewFilmeForm(request.POST, usuario=request.user)

        if form.is_valid():
            review = form.save(commit=False)
            review.usuario = request.user
            review.save()
            return redirect('gestao:index')
        
    return render(
        request,
        'register.html',
        {
            'form': form
        }
    )

def createreviewserie(request):
    form = ReviewSeriesForm(usuario=request.user)

    if request.method == 'POST':
        form = ReviewSeriesForm(request.POST, usuario=request.user)

        if form.is_valid():
            review = form.save(commit=False)
            review.usuario = request.user
            review.save()
            return redirect('gestao:index')
        
    return render(
        request,
        'register.html',
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
        'register.html',
        {
            'form': form,
            'site_title': 'Criar Noticias'
        }
    )

def createserie(request):
    form = SeriesForm()

    if request.method == 'POST':
        form = SeriesForm(request.POST, request.FILES)

        if form.is_valid():
            review = form.save(commit=False)
            review.save()
            return redirect('gestao:listarseries')
        
    return render(
        request,
        'register.html',
        {
            'form': form,
            'site_title': 'Criar Série'
        }
    )

def updatefilme(request, filme_id):
    try:
        single_filme = Filmes.objects.get(pk=filme_id)
    except Filmes.DoesNotExist:
        return redirect('gestao:index')
        

    form_action = reverse('gestao:updatefilme', args=(filme_id,))

    if request.method == 'POST':
        form = FilmesForm(request.POST, request.FILES, instance=single_filme)

        context = {
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            filme = form.save()
            return redirect('gestao:infofilme', filme_id=filme.pk)

        return render(
            request,
            'register.html',
            context
        )

    context = {
        'form': FilmesForm(instance=single_filme),
        'form_action': form_action,
    }

    return render(
        request,
        'register.html',
        context
    )

def updateserie(request, serie_id):
    try:
        single_serie = Series.objects.get(pk=serie_id)
    except Series.DoesNotExist:
        return redirect('gestao:index')
        

    form_action = reverse('gestao:updateserie', args=(serie_id,))

    if request.method == 'POST':
        form = SeriesForm(request.POST, request.FILES, instance=single_serie)

        context = {
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            serie = form.save()
            return redirect('gestao:infoserie', serie_id=serie.pk)

        return render(
            request,
            'register.html',
            context
        )

    context = {
        'form': SeriesForm(instance=single_serie),
        'form_action': form_action,
    }

    return render(
        request,
        'register.html',
        context
    )

def updatenoticia(request, noticia_id):
    try:
        single_noticia = Noticias.objects.get(pk=noticia_id)
    except Noticias.DoesNotExist:
        return redirect('gestao:index')
        

    form_action = reverse('gestao:updatenoticia', args=(noticia_id,))

    if request.method == 'POST':
        form = NoticiasForm(request.POST, request.FILES, instance=single_noticia)

        context = {
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            form.save()
            return redirect('gestao:index')

        return render(
            request,
            'register.html',
            context
        )

    context = {
        'form': NoticiasForm(instance=single_noticia),
        'form_action': form_action,
    }

    return render(
        request,
        'register.html',
        context
    )

def updatereviewfilme(request, review_id):
    try:
        single_reviewfilme = ReviewsFilmes.objects.get(pk=review_id)
    except ReviewsFilmes.DoesNotExist:
        return redirect('gestao:index')
        
    if single_reviewfilme.usuario == request.user:
        form_action = reverse('gestao:updatereviewfilme', args=(review_id,))

        if request.method == 'POST':
            form = ReviewUpdateFilmeForm(request.POST, instance=single_reviewfilme)

            context = {
                'form': form,
                'form_action': form_action,
            }

            if form.is_valid():
                form.save()
                return redirect('gestao:index')

            return render(
                request,
                'register.html',
                context
            )

        context = {
            'form': ReviewUpdateFilmeForm(instance=single_reviewfilme),
            'form_action': form_action,
        }

        return render(
            request,
            'register.html',
            context
        )
    else:
        return redirect('gestao:inforeviewfilme', review_id=single_reviewfilme.pk)

def updatereviewserie(request, review_id):
    try:
        single_reviewserie = ReviewsSeries.objects.get(pk=review_id)
    except ReviewsSeries.DoesNotExist:
        return redirect('gestao:index')
        
    if single_reviewserie.usuario == request.user:
        form_action = reverse('gestao:updatereviewserie', args=(review_id,))

        if request.method == 'POST':
            form = ReviewUpdateSeriesForm(request.POST, instance=single_reviewserie)

            context = {
                'form': form,
                'form_action': form_action,
            }

            if form.is_valid():
                form.save()
                return redirect('gestao:index')

            return render(
                request,
                'register.html',
                context
            )

        context = {
            'form': ReviewUpdateSeriesForm(instance=single_reviewserie),
            'form_action': form_action,
        }

        return render(
            request,
            'register.html',
            context
        )
    else:
        return redirect('gestao:inforeviewserie', review_id=single_reviewserie.pk)


def listarfilmes(request):
    try:

        filmes = Filmes.objects \
            .order_by('-id') \
            .distinct() 

        paginator = Paginator(filmes, 6)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        context = {
            'redirect': 'gestao:infofilme',
            'items': filmes,
            'page_obj': page_obj,
            'site_title': 'Filmes'
        }

        return render(
            request,
            'listar.html',
            context
        )
    
    except AttributeError:
        context = {
            'site_title': 'Filmes'
        }

        return render(
            request,
            'listar.html',
            context
        )
    
def listarseries(request):
    try:
        series = Series.objects \
        .order_by('-id')\
        .distinct()

        paginator = Paginator(series, 6)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        context = {
            'redirect': 'gestao:infoserie',
            'items': series,
            'page_obj': page_obj,
            'site_title': 'Séries'
        }

        return render(
            request,
            'listar.html',
            context
        )
    
    except AttributeError:
        context = {
            'site_title': 'Séries'
        }

        return render(
            request,
            'listar.html',
            context
        )
    
def deletefilme(request, filme_id):
    if request.user.is_admin:
        single_filme = Filmes.objects.get(pk=filme_id)
        single_filme.delete()
        return redirect('gestao:listarfilmes')
    else:
        return redirect('gestao:listarfilmes')

def deleteserie(request, serie_id):
    if request.user.is_admin:
        single_serie = Series.objects.get(pk=serie_id)
        single_serie.delete()
        return redirect('gestao:listarseries')
    else:
        return redirect('gestao:listarseries')

def deletenoticia(request, noticia_id):
    if request.user.is_admin:
        single_noticia = Noticias.objects.get(pk=noticia_id)
        single_noticia.delete()
        return redirect('gestao:index')
    else:
        return redirect('gestao:index')

def deletereviewfilme(request, review_id):
    if request.user.is_admin:
        single_review= ReviewsFilmes.objects.get(pk=review_id)
        single_review.delete()
        return redirect('gestao:listarfilmes')
    else:
        return redirect('gestao:listarfilmes')

def deletereviewserie(request, review_id):
    if request.user.is_admin:
        single_review = ReviewsSeries.objects.get(pk=review_id)
        single_review.delete()
        return redirect('gestao:listarseries')
    else:
        return redirect('gestao:listarfilmes')

def infouser(request, user_id):
    try:
        single_user = CustomUser.objects.get(pk=user_id)
    except CustomUser.DoesNotExist:
        return redirect('gestao:index')

    site_title = f'{single_user.username} - '

    context = {
        'usuario': single_user,
        'site_title': site_title
    }

    return render(
        request,
        'info.html',
        context
    )

def infofilme(request, filme_id):
    try:
        single_filme = Filmes.objects.get(pk=filme_id)
    except Filmes.DoesNotExist:
        return redirect('gestao:index')
    
    reviews = ReviewsFilmes.objects \
        .filter(mostrar=True, filme_id = single_filme)\
        .order_by('-id')

    paginator = Paginator(reviews, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

        
    site_title = f'{single_filme.nome} - {single_filme.data.year}'

    context = {
        'update': 'gestao:updatefilme',
        'counterlink': 'gestao:inforeviewfilme',
        'reviews': reviews,
        'page_obj': page_obj,
        'item': single_filme,
        'site_title': site_title
    }

    return render(
        request,
        'info.html',
        context
    )

def infoserie(request, serie_id):
    try:
        single_serie = Series.objects.get(pk=serie_id)
    except Series.DoesNotExist:
        return redirect('gestao:index')
    
    reviews = ReviewsSeries.objects \
        .filter(mostrar=True, serie_id = single_serie)\
        .order_by('-id')

    paginator = Paginator(reviews, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
        
    site_title = f'{single_serie.nome} - {single_serie.data.year}'

    context = {
        'update': 'gestao:updateserie',
        'counterlink': 'gestao:inforeviewserie',
        'reviews': reviews,
        'page_obj': page_obj,
        'item': single_serie,
        'site_title': site_title
    }

    return render(
        request,
        'info.html',
        context
    )

def inforeviewfilme(request, review_id):
    try:
        single_review = ReviewsFilmes.objects.get(pk=review_id)
    except ReviewsFilmes.DoesNotExist:
        return redirect('gestao:index')
    
    site_title = f'{single_review.usuario} - {single_review.nota}'

    context = {
        'update': 'gestao:updatereviewfilme',
        'Fonte': 'Filme',
        'fonte': single_review.filme,
        'review': single_review,
        'site_title': site_title
    }

    return render(
        request,
        'info.html',
        context
    )

def inforeviewserie(request, review_id):
    try:
        single_review = ReviewsSeries.objects.get(pk=review_id)
    except ReviewsSeries.DoesNotExist:
        return redirect('gestao:index')
    
    site_title = f'{single_review.usuario} - {single_review.nota}'

    context = {
        'update': 'gestao:updatereviewserie',
        'Fonte': 'Série',
        'fonte': single_review.serie,
        'review': single_review,
        'site_title': site_title
    }

    return render(
        request,
        'info.html',
        context
    )