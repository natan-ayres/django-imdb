from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.urls import reverse
import requests
from django.contrib import auth
from . models import Noticias, Filmes, ReviewsFilmes, ReviewsSeries, Series, CustomUser, Grupos
from . forms import RegisterUpdateForm, RegisterForm, CustomAuthenticationForm, FilmesForm, ReviewFilmeForm, ReviewFilmeFiltroForm, ReviewUpdateFilmeForm, ReviewSeriesForm, ReviewUpdateSeriesForm, NoticiasForm, SeriesForm, GruposForm, ApiForm, ReviewSerieFiltroForm

from IMDB.local_settings import api_key

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
            'countertext': 'No Account Yet? Sign-up here',
            'counterlink': 'gestao:register',
            'botao': 'Join',
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
            'countertext': 'Already Have an Account? Join Here!',
            'counterlink': 'gestao:login',
            'botao': 'Sign-up',
            'site_title': 'Register',
            'form': form
        }
    )

def update(request):   
    if request.user:
        usuario = request.user
        form_action = reverse('gestao:update')

        if request.method == 'POST':
            form = RegisterUpdateForm(request.POST, instance=usuario)

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
            'form': RegisterUpdateForm(instance=usuario),
            'form_action': form_action,
        }

        return render(
            request,
            'register.html',
            context
        )
    else:
        return redirect('gestao:index')
    
def deleteview(request):
    if request.user:
        usuario = request.user
        usuario.delete()
        return redirect('gestao:index')
    else:
        return redirect('gestao:index')


def logoutview(request):
    if request.user:
        auth.logout(request)
        return redirect('gestao:login')
    else:
        return redirect('gestao:index')

def createfilme(request):
    if request.user.is_admin:
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
                'form': form,
                'site_title': 'Criar Filme'
            }
        )
    else:
        return redirect('gestao:index')

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
            'form': form,
            'site_title': 'Criar Review'
        }
    )

def createreviewfilmefiltro(request, filme_id):
    try:
        single_filme = Filmes.objects.get(pk=filme_id)
    except Filmes.DoesNotExist:
        return redirect('gestao:index')
    form = ReviewFilmeFiltroForm()


    if request.method == 'POST':
        form = ReviewFilmeFiltroForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.usuario = request.user
            review.filme = single_filme
            review.save()
            return redirect('gestao:index')
        
    return render(
        request,
        'register.html',
        {
            'form': form,
            'site_title': 'Criar Review'
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
            'form': form,
            'site_title': 'Criar Review'
        }
    )

def createreviewseriefiltro(request, serie_id):
    try:
        single_serie = Series.objects.get(pk=serie_id)
    except Series.DoesNotExist:
        return redirect('gestao:index')
    form = ReviewSerieFiltroForm()


    if request.method == 'POST':
        form = ReviewSerieFiltroForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.usuario = request.user
            review.serie = single_serie
            review.save()
            return redirect('gestao:index')
        
    return render(
        request,
        'register.html',
        {
            'form': form,
            'site_title': 'Criar Review'
        }
    )

def createnoticia(request):
    if request.user.is_admin:
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
                'site_title': 'Criar - Noticia'
            }
        )
    else:
        return redirect('gestao:index')

def createserie(request):
    if request.user.is_admin:
        form = SeriesForm()

        if request.method == 'POST':
            form = SeriesForm(request.POST, request.FILES)

            if form.is_valid():
                serie = form.save(commit=False)
                serie.save()
                return redirect('gestao:listarseries')
            
        return render(
            request,
            'register.html',
            {
                'form': form,
                'site_title': 'Criar Série'
            }
        )
    else:
        return redirect('gestao:index')
    
def creategrupo(request):
    form = GruposForm()

    if request.method == 'POST':
        form = GruposForm(request.POST, request.FILES)

        if form.is_valid():
            grupo = form.save(commit=False)
            grupo.dono = request.user
            grupo.save()
            return redirect('gestao:index')
        
    return render(
        request,
        'register.html',
        {
            'form': form,
            'site_title': 'Criar Grupo'
        }
    )

def updatefilme(request, filme_id):
    if request.user.is_admin:
        try:
            single_filme = Filmes.objects.get(pk=filme_id)
        except Filmes.DoesNotExist:
            return redirect('gestao:index')
            

        form_action = reverse('gestao:updatefilme', args=(filme_id,))

        site_title = f'{single_filme.nome} - {single_filme.data.year}'

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
            'site_title': site_title,
        }

        return render(
            request,
            'register.html',
            context
        )
    else:
        return redirect('gestao:index')

def updateserie(request, serie_id):
    if request.user.is_admin:
        try:
            single_serie = Series.objects.get(pk=serie_id)
            site_title = f'{single_serie.nome} - {single_serie.data.year}'
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
            'site_title': site_title, 
        }

        return render(
            request,
            'register.html',
            context
        )
    else:
        return redirect('gestao:index')

def updatenoticia(request, noticia_id):
    if request.user.is_admin:
        try:
            single_noticia = Noticias.objects.get(pk=noticia_id)
            site_title = f'{single_noticia.nome} - {single_noticia.data.day}/{single_noticia.data.month}'
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
            'site_title': site_title,
        }

        return render(
            request,
            'register.html',
            context
        )
    else:
        return redirect('gestao:index')
    
 

def updatereviewfilme(request, review_id):
    try:
        single_review = ReviewsFilmes.objects.get(pk=review_id)
        site_title = f'{single_review.usuario} - {single_review.nota}'
    except ReviewsFilmes.DoesNotExist:
        return redirect('gestao:index')
        
    if single_review.usuario == request.user:
        form_action = reverse('gestao:updatereviewfilme', args=(review_id,))

        if request.method == 'POST':
            form = ReviewUpdateFilmeForm(request.POST, instance=single_review)

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
            'form': ReviewUpdateFilmeForm(instance=single_review),
            'form_action': form_action,
            'site_title': site_title,
        }

        return render(
            request,
            'register.html',
            context
        )
    else:
        return redirect('gestao:index')

def updatereviewserie(request, review_id):
    try:
        single_review = ReviewsSeries.objects.get(pk=review_id)
        site_title = f'{single_review.usuario} - {single_review.nota}'
    except ReviewsSeries.DoesNotExist:
        return redirect('gestao:index')
        
    if single_review.usuario == request.user:
        form_action = reverse('gestao:updatereviewserie', args=(review_id,))

        if request.method == 'POST':
            form = ReviewUpdateSeriesForm(request.POST, instance=single_review)

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
            'form': ReviewUpdateSeriesForm(instance=single_review),
            'form_action': form_action,
            'site_title': site_title,
        }

        return render(
            request,
            'register.html',
            context
        )
    else:
        return redirect('gestao:index')
    
def updategrupo(request, grupo_id):
    try:
        single_grupo = Grupos.objects.get(pk=grupo_id)
        site_title = f'{single_grupo.nome}'
    except Grupos.DoesNotExist:
        return redirect('gestao:index')
    
    if single_grupo.dono == request.user:
        form_action = reverse('gestao:updategrupo', args=(grupo_id,))

        if request.method == 'POST':
            form = GruposForm(request.POST, instance=single_grupo)

            context = {
                'form': form,
                'form_action': form_action
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
            'form': GruposForm(instance=single_grupo),
            'form_action': form_action,
            'site_title': site_title,
        }

        return render(
            request,
            'register.html',
            context
        )
    else:
        return redirect('gestao:index')
        
def adicionarwaitlist(request, grupo_id):
    single_grupo = Grupos.objects.get(pk=grupo_id)
    usuario_esta_na_waitlist = single_grupo.waitlist.filter(id=request.user.id).exists()
    if usuario_esta_na_waitlist == False and request.user != single_grupo.dono:
        single_grupo.waitlist.add(request.user)
    return redirect('gestao:infogrupo', grupo_id=single_grupo.pk)

def adicionarmembro(request, grupo_id, user_id):
    single_grupo = Grupos.objects.get(pk=grupo_id)
    if request.user == single_grupo.dono:
        usuario_esta_no_grupo = single_grupo.membros.filter(id=user_id).exists()
        if usuario_esta_no_grupo == False:
            single_grupo.membros.add(user_id)
            single_grupo.qntdmembros += 1
            single_grupo.waitlist.remove(user_id)
            single_grupo.save()
    return redirect('gestao:infogrupo', grupo_id=single_grupo.pk)

def listarfilmes(request):
    try:

        filmes = Filmes.objects \
            .order_by('-id') \
            .distinct() 

        context = {
            'create': 'gestao:apifilmes',
            'redirect': 'gestao:infofilme',
            'items': filmes,
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
    
def listarfilmesgrupo(request, grupo_id):
    try:
        single_grupo = Grupos.objects.get(pk=grupo_id)
        filmes_avaliados = Filmes.objects.filter(
        reviews__usuario__in=single_grupo.membros.all()
        ).distinct()

        contador = 0
        nota = 0
        notas = []
        filmes_com_notas = []
        
        membros = CustomUser.objects \
                .filter(membros = single_grupo)\
                .order_by('-id')
        
        for filme in filmes_avaliados:
            contador = 0
            nota = 0
            reviews = ReviewsFilmes.objects \
                .filter(filme=filme.id,)\
                .order_by('-id')
            for review in reviews:
                for membro in membros:
                    if review.usuario == membro:
                        nota += review.nota
                        contador += 1
            if contador > 0: 
                nota = nota / contador
                notas.append(nota)
            else:
                notas.append('?')

            filmes_com_notas.append((filme, notas[-1]))
        

        context = {
            'create': 'gestao:apifilmes',
            'redirect': 'gestao:infofilmegrupo',
            'items_notas': filmes_com_notas,
            'site_title': 'Filmes',
            'grupo_id': grupo_id,
            'notas': notas,
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

        context = {
            'create': 'gestao:apiseries',
            'redirect': 'gestao:infoserie',
            'items': series,
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
    
def listarseriesgrupo(request, grupo_id):
    try:
        single_grupo = Grupos.objects.get(pk=grupo_id)
        series_avaliadas = Series.objects.filter(
        reviews__usuario__in=single_grupo.membros.all()
        ).distinct()

        contador = 0
        nota = 0
        notas = []
        series_com_notas = []
        
        membros = CustomUser.objects \
                .filter(membros = single_grupo)\
                .order_by('-id')
        
        for serie in series_avaliadas:
            contador = 0
            nota = 0
            reviews = ReviewsSeries.objects \
                .filter(serie=serie.id,)\
                .order_by('-id')
            for review in reviews:
                for membro in membros:
                    if review.usuario == membro:
                        nota += review.nota
                        contador += 1
            if contador > 0: 
                nota = nota / contador
                notas.append(nota)
            else:
                notas.append('?')

            series_com_notas.append((serie, notas[-1]))
        

        context = {
            'create': 'gestao:apiseries',
            'redirect': 'gestao:infoseriegrupo',
            'items_notas': series_com_notas,
            'site_title': 'Series',
            'grupo_id': grupo_id,
            'notas': notas,
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
    
def listargrupos(request):
    try:
        grupos = Grupos.objects \
        .order_by('-id')\
        .distinct()

        paginator = Paginator(grupos, 6)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        context = {
            'create': 'gestao:criargrupo',
            'grupos': grupos,
            'page_obj': page_obj,
            'site_title': 'Grupos'
        }

        return render(
            request,
            'listar.html',
            context
        )
    except AttributeError:
        context = {
            'site_title': 'Grupos'
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
    

def deleteserie(request, serie_id):
    if request.user.is_admin:
        single_serie = Series.objects.get(pk=serie_id)
        single_serie.delete()
    return redirect('gestao:listarseries')

def deletenoticia(request, noticia_id):
    if request.user.is_admin:
        single_noticia = Noticias.objects.get(pk=noticia_id)
        single_noticia.delete()
    return redirect('gestao:index')


def deletereviewfilme(request, review_id):
    try:
        single_review= ReviewsFilmes.objects.get(pk=review_id)
    except ReviewsFilmes.DoesNotExist:
        return redirect('gestao:index')
    if request.user.is_admin or request.user == single_review.usuario:
        single_review.delete()
    return redirect('gestao:listarfilmes')

def deletereviewserie(request, review_id):
    try:
        single_review= ReviewsSeries.objects.get(pk=review_id)
    except ReviewsSeries.DoesNotExist:
        return redirect('gestao:index')
    if request.user.is_admin or request.user == single_review.usuario:
        single_review.delete()
    return redirect('gestao:listarseries')
    
def deletegrupo(request, grupo_id):
    try:
        single_grupo = Grupos.objects.get(pk=grupo_id)
    except Grupos.DoesNotExist:
        return redirect('gestao:index')
    if single_grupo.dono == request.user or request.user.is_admin:
        single_grupo.delete()
        return redirect('gestao:listargrupos')
    else:
        return redirect('gestao:listargrupos')
    
def removermembro(request, user_id, grupo_id):
    try:
        single_grupo = Grupos.objects.get(pk=grupo_id)
    except Grupos.DoesNotExist:
        return redirect('gestao:index')
    if single_grupo.dono == request.user:
        single_grupo.membros.remove(user_id)
        single_grupo.qntdmembros += -1
        if single_grupo.qntdmembros < 0: 
            single_grupo.qntdmembros = 0
        single_grupo.save()
    return redirect('gestao:infogrupo', grupo_id=single_grupo.pk)
    
def negarwaitlist(request, grupo_id, user_id):
    try:
        single_grupo = Grupos.objects.get(pk=grupo_id)
    except Grupos.DoesNotExist:
        return redirect('gestao:index')
    if request.user == single_grupo.dono:
        usuario_esta_na_waitlist = single_grupo.waitlist.filter(id=user_id).exists()
        if usuario_esta_na_waitlist == True:
            single_grupo.waitlist.remove(user_id)
    return redirect('gestao:infogrupo', grupo_id=single_grupo.pk)

def infouser(request, user_id):
    try:
        single_user = CustomUser.objects.get(pk=user_id)
    except CustomUser.DoesNotExist:
        return redirect('gestao:index')
    
    try:
        reviewsfilmes = ReviewsFilmes.objects \
        .filter(usuario=user_id)\
        .order_by('-id')\
        .distinct()
    except AttributeError:
        reviewsfilmes = None

    try:
        reviewsseries = ReviewsSeries.objects \
        .filter(usuario=user_id)\
        .order_by('-id')\
        .distinct()
    except AttributeError:
        reviewsseries = None

    site_title = f'{single_user.username} - '

    context = {
        'reviewsfilmes': reviewsfilmes,
        'reviewsseries': reviewsseries,
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
        'nota': single_filme.nota_media,
        'delete': 'gestao:deletefilme',
        'update': 'gestao:updatefilme',
        'counterlink': 'gestao:inforeviewfilme',
        'titulo': 'REVIEWS',
        'users': reviews,
        'page_obj': page_obj,
        'item': single_filme,
        'site_title': site_title,
        'infoitem': True,
        'create': 'gestao:criarreviewfilmefiltro',
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
        'nota': single_serie.nota_media,
        'delete': 'gestao:deleteserie',
        'update': 'gestao:updateserie',
        'counterlink': 'gestao:inforeviewserie',
        'users': reviews,
        'titulo': 'REVIEWS',
        'page_obj': page_obj,
        'item': single_serie,
        'site_title': site_title,
        'infoitem': True,
        'create': 'gestao:criarreviewseriefiltro',
    }

    return render(
        request,
        'info.html',
        context
    )

def infonoticia(request, noticia_id):
    try:
        single_noticia = Noticias.objects.get(pk=noticia_id)
    except Noticias.DoesNotExist:
        return redirect('gestao:index')
    
    site_title = f'{single_noticia.nome} - {single_noticia.data.day}/{single_noticia.data.month}'

    context = {
        'noticia': single_noticia,
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
        'delete': 'gestao:deletereviewfilme',
        'update': 'gestao:updatereviewfilme',
        'Fonte': 'Filme',
        'info': 'gestao:infofilme',
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
        'delete': 'gestao:deletereviewserie',
        'update': 'gestao:updatereviewserie',
        'Fonte': 'Série',
        'info': 'gestao:infoserie',
        'fonte': single_review.serie,
        'review': single_review,
        'site_title': site_title
    }

    return render(
        request,
        'info.html',
        context
    )

def infogrupo(request, grupo_id):
    try:
        single_grupo = Grupos.objects.get(pk=grupo_id)
    except Grupos.DoesNotExist:
        return redirect('gestao:index')

    usuario_esta_na_waitlist = single_grupo.waitlist.filter(id=request.user.id).exists()   
    usuario_e_membro = single_grupo.membros.filter(id=request.user.id).exists()   
    filmes_avaliados = Filmes.objects.filter(
        reviews__usuario__in=single_grupo.membros.all()
    ).distinct()
    series_avaliados = Series.objects.filter(
        reviews__usuario__in=single_grupo.membros.all()
    ).distinct()

    contador_filmes = 0
    contador_series = 0

    for filmes in filmes_avaliados:
        contador_filmes += 1

    for serie in series_avaliados:
        contador_series += 1

    if request.user == single_grupo.dono:
        waitlist = CustomUser.objects \
            .filter(waitlist = single_grupo)\
            .order_by('-id')


        paginator = Paginator(waitlist, 10)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

    else:
        waitlist = None
        page_number = None
        page_obj = None

    site_title = f'{single_grupo.nome}'

    context = {
        'users': waitlist,
        'waitlist': True,
        'titulo': 'WAITLIST',
        'page_obj': page_obj,
        'user_membro': usuario_e_membro,
        'user_waitlist': usuario_esta_na_waitlist,
        'grupo': single_grupo,
        'site_title': site_title,
        'filmes_avaliados': filmes_avaliados,
        'contador_filmes': contador_filmes,
        'contador_series': contador_series,
    }

    return render(
        request,
        'info.html',
        context
    )

def infomembros(request, grupo_id):
    single_grupo = Grupos.objects.get(pk=grupo_id)
    usuario_esta_no_grupo = single_grupo.membros.filter(id=request.user.id).exists()
    if usuario_esta_no_grupo == True or request.user == single_grupo.dono:
        try:
            single_grupo = Grupos.objects.get(pk=grupo_id)
        except Grupos.DoesNotExist:
            return redirect('gestao:index')
        
        membros = CustomUser.objects \
                .filter(membros = single_grupo)\
                .order_by('-id')

        site_title = f'Membros de {single_grupo.nome}'

        context = {
            'grupos': single_grupo,
            'membros': membros,
            'site_title': site_title,
        }

        return render(
            request,
            'info.html',
            context
        )
    else:
        return redirect('gestao:index')

def infofilmegrupo(request, grupo_id, filme_id):
    single_grupo = Grupos.objects.get(pk=grupo_id)
    usuario_esta_no_grupo = single_grupo.membros.filter(id=request.user.id).exists()
    if usuario_esta_no_grupo == True or request.user == single_grupo.dono:
        try:
            single_filme = Filmes.objects.get(pk=filme_id)
        except Grupos.DoesNotExist or Filmes.DoesNotExist:
            return redirect('gestao:index')
        
        reviews = ReviewsFilmes.objects \
                .filter(filme=filme_id,)\
                .order_by('-id')
        
        membros = CustomUser.objects \
                .filter(membros = single_grupo)\
                .order_by('-id') 
        
        contador = 0
        nota = 0

        for review in reviews:
            for membro in membros:
                if review.usuario == membro:
                    nota += review.nota
                    contador += 1

        try: 
            nota = nota / contador
        except ZeroDivisionError:
            nota = 'N/A'
    else:
        return redirect('gestao:index')

    return render(request, 'info.html', {'item': single_filme, 'nota': nota})

def infoseriegrupo(request, grupo_id, serie_id):
    single_grupo = Grupos.objects.get(pk=grupo_id)
    usuario_esta_no_grupo = single_grupo.membros.filter(id=request.user.id).exists()
    if usuario_esta_no_grupo == True or request.user == single_grupo.dono:
        try:
            single_serie = Series.objects.get(pk=serie_id)
        except Grupos.DoesNotExist or Series.DoesNotExist:
            return redirect('gestao:index')
        
        reviews = ReviewsSeries.objects \
                .filter(serie=serie_id,)\
                .order_by('-id')
        
        membros = CustomUser.objects \
                .filter(membros = single_grupo)\
                .order_by('-id') 
        
        contador = 0
        nota = 0

        for review in reviews:
            for membro in membros:
                if review.usuario == membro:
                    nota += review.nota
                    contador += 1

        try: 
            nota = nota / contador
        except ZeroDivisionError:
            nota = 'N/A'
    else:
        return redirect('gestao:index')
    
    return render(request, 'info.html', {'item': single_serie, 'nota': nota})

def apifilmes(request):
    if request.user.is_admin: 
        form = ApiForm()
        buscado = False
        if request.method == 'POST':
            form = ApiForm(request.POST)
            if form.is_valid():
                nome = form.cleaned_data['nome']
                ano = form.cleaned_data['ano']

                if ano:
                    response = requests.get(f'https://www.omdbapi.com/?t={nome}&type=movie&y={ano}&apikey={api_key}')
                else:
                    response = requests.get(f'https://www.omdbapi.com/?t={nome}&type=movie&apikey={api_key}')

                if response.status_code == 200:
                    dados_api = response.json()
                    nome = dados_api.get('Title')
                    diretor = dados_api.get('Director')
                    escritor = dados_api.get('Writer')
                    atores = dados_api.get('Actors')
                    poster = dados_api.get('Poster')
                    sinopse = dados_api.get('Plot')
                    classificacao = dados_api.get('Rated'),
                    classificacao_limpa = classificacao[0]
                    data = dados_api.get('Released')
                    duracao = dados_api.get('Runtime')
                    if 'submit_primeiro' in request.POST and nome != None:
                        buscado = True
                        return render(request, 'register.html', {'form':form, 'api': True, 'apinome': nome, 'apidiretor': diretor, 'apiposter': poster, 'apisinopse': sinopse, 'apiclassificacao': classificacao_limpa, 'apidata': data, 'apiduracao': duracao, 'buscado': buscado, 'apiatores': atores, 'apiescritor': escritor})
                    if 'submit_segundo' in request.POST:
                        Filmes.objects.create(
                            nome = nome,
                            diretor = diretor,
                            escritor = escritor,
                            poster = poster,
                            classificacao = classificacao_limpa,
                            atores = atores,
                            sinopse = sinopse,
                            data = data,
                            duracao = duracao,
                        )
                        return redirect('gestao:listarfilmes')
                    if 'submit_terceiro' in request.POST:
                        return redirect('gestao:apifilmes')
                    elif 'submit_quarto' in request.POST:
                        return redirect('gestao:criarfilme')
    else:
        return redirect('gestao:index')

        
    return render(request, 'register.html', {'form':form, 'buscado': buscado, 'api':True})


def apiseries(request):
    if request.user.is_admin: 
        form = ApiForm()
        buscado = False
        if request.method == 'POST':
            form = ApiForm(request.POST)
            if form.is_valid():
                nome = form.cleaned_data['nome']
                ano = form.cleaned_data['ano']

                if ano:
                    response = requests.get(f'https://www.omdbapi.com/?t={nome}&type=series&y={ano}&apikey={api_key}')
                else:
                    response = requests.get(f'https://www.omdbapi.com/?t={nome}&type=series&apikey={api_key}')

                if response.status_code == 200:
                    dados_api = response.json()
                    nome = dados_api.get('Title')
                    diretor = dados_api.get('Director')
                    escritor = dados_api.get('Writer')
                    atores = dados_api.get('Actors')
                    poster = dados_api.get('Poster')
                    classificacao = dados_api.get('Rated')
                    classificacao_limpa = classificacao[0]
                    sinopse = dados_api.get('Plot')
                    data = dados_api.get('Released')
                    temporadas = dados_api.get('totalSeasons')
                    if 'submit_primeiro' in request.POST and nome != None:
                        buscado = True
                        return render(request, 'register.html', {'form':form, 'api': True, 'apinome': nome, 'apidiretor': diretor, 'apiposter': poster, 'apisinopse': sinopse, 'apidata': data,'apiclassificacao': classificacao_limpa, 'apitemporadas': temporadas, 'buscado': buscado, 'apiatores': atores, 'apiescritor': escritor})
                    elif 'submit_segundo' in request.POST:
                        Series.objects.create(
                            nome = nome,
                            diretor = diretor,
                            escritor = escritor,
                            poster = poster,
                            classificacao = classificacao_limpa,
                            atores = atores,
                            sinopse = sinopse,
                            data = data,
                            temporadas = temporadas,
                        )
                        return redirect('gestao:listarseries')
                    elif 'submit_terceiro' in request.POST:
                        return redirect('gestao:apiseries')
                    elif 'submit_quarto' in request.POST:
                        return redirect('gestao:criarserie')
    else:
        return redirect('gestao:index')

        
    return render(request, 'register.html', {'form':form, 'buscado': buscado, 'api':True})