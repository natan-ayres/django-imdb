from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.urls import reverse
import requests
from django.contrib import auth
from . models import News, Movies, ReviewsMovies, ReviewsSeries, Series, CustomUser, Groups
from . forms import RegisterUpdateForm, RegisterForm, CustomAuthenticationForm, MoviesForm, ReviewMovieForm, ReviewUpdateMovieForm, ReviewSeriesForm, ReviewUpdateSeriesForm, NewsForm, SeriesForm, GroupsForm, ApiForm

from IMDB.local_settings import api_key

def index(request):
    try:

        news = News.objects \
            .filter(show = True) \
            .order_by('-date') \
            .distinct() 

        context = {
            'news': news,
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
            'countertext': 'No account yet? Sign-in here!',
            'counterlink': 'gestao:register',
            'botao': 'Login',
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
            'countertext': 'Already have an Account? Login here!',
            'counterlink': 'gestao:login',
            'botao': 'Sign-in',
            'site_title': 'Register',
            'form': form
        }
    )

def update(request):   
    if request.user:
        user = request.user
        form_action = reverse('gestao:update')

        if request.method == 'POST':
            form = RegisterUpdateForm(request.POST, instance=user)

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
            'form': RegisterUpdateForm(instance=user),
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
        user = request.user
        user.delete()
        return redirect('gestao:index')
    else:
        return redirect('gestao:index')


def logoutview(request):
    if request.user:
        auth.logout(request)
        return redirect('gestao:login')
    else:
        return redirect('gestao:index')

def createmovie(request):
    if request.user.is_admin:
        form = MoviesForm()
        
        if request.method == 'POST':
            form = MoviesForm(request.POST, request.FILES)

            if form.is_valid():
                form.save()
                return redirect('gestao:listmovies')
            
        return render(
            request,
            'register.html',
            {
                'form': form,
                'site_title': 'Create Movie'
            }
        )
    return redirect('gestao:index')

def createreviewmovie(request):
    form = ReviewMovieForm(user=request.user)

    if request.method == 'POST':
        form = ReviewMovieForm(request.POST, user=request.user)

        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('gestao:index')
        
    return render(
        request,
        'register.html',
        {
            'form': form,
            'site_title': 'Create Review'
        }
    )


def createreviewserie(request):
    form = ReviewSeriesForm(user=request.user)

    if request.method == 'POST':
        form = ReviewSeriesForm(request.POST, user=request.user)

        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('gestao:index')
        
    return render(
        request,
        'register.html',
        {
            'form': form,
            'site_title': 'Create Review'
        }
    )

def createnews(request):
    if request.user.is_admin:
        form = NewsForm()

        if request.method == 'POST':
            form = NewsForm(request.POST,  request.FILES)

            if form.is_valid():
                news = form.save(commit=False)
                news.user = request.user
                news.save()
                return redirect('gestao:index')
            
        
        return render(
            request,
            'register.html',
            {
                'form': form,
                'site_title': 'Create News'
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
                return redirect('gestao:listseries')
            
        return render(
            request,
            'register.html',
            {
                'form': form,
                'site_title': 'Create Serie'
            }
        )
    else:
        return redirect('gestao:index')
    
def creategroup(request):
    form = GroupsForm()

    if request.method == 'POST':
        form = GroupsForm(request.POST, request.FILES)

        if form.is_valid():
            group = form.save(commit=False)
            group.owner = request.user
            group.save()
            return redirect('gestao:index')
        
    return render(
        request,
        'register.html',
        {
            'form': form,
            'site_title': 'Create Group'
        }
    )

def updatemovie(request, movie_id):
    if request.user.is_admin:
        try:
            single_movie = Movies.objects.get(pk=movie_id)
        except Movies.DoesNotExist:
            return redirect('gestao:index')
            

        form_action = reverse('gestao:updatemovie', args=(movie_id,))

        site_title = f'{single_movie.name} - {single_movie.date.year}'

        if request.method == 'POST':
            form = MoviesForm(request.POST, request.FILES, instance=single_movie)

            context = {
                'form': form,
                'form_action': form_action,
            }

            if form.is_valid():
                movie = form.save()
                return redirect('gestao:infomovie', movie_id=movie.pk)

            return render(
                request,
                'register.html',
                context
            )

        context = {
            'form': MoviesForm(instance=single_movie),
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
            site_title = f'{single_serie.name} - {single_serie.date.year}'
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

def updatenews(request, news_id):
    if request.user.is_admin:
        try:
            single_news = News.objects.get(pk=news_id)
            site_title = f'{single_news.name} - {single_news.date.day}/{single_news.date.month}'
        except News.DoesNotExist:
            return redirect('gestao:index')
            

        form_action = reverse('gestao:updatenews', args=(news_id,))

        if request.method == 'POST':
            form = NewsForm(request.POST, request.FILES, instance=single_news)

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
            'form': NewsForm(instance=single_news),
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
    
 

def updatereviewmovie(request, review_id):
    try:
        single_review = ReviewsMovies.objects.get(pk=review_id)
        site_title = f'{single_review.user} - {single_review.grade}'
    except ReviewsMovies.DoesNotExist:
        return redirect('gestao:index')
        
    if single_review.user == request.user:
        form_action = reverse('gestao:updatereviewmovie', args=(review_id,))

        if request.method == 'POST':
            form = ReviewUpdateMovieForm(request.POST, instance=single_review)

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
            'form': ReviewUpdateMovieForm(instance=single_review),
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
        site_title = f'{single_review.user} - {single_review.grade}'
    except ReviewsSeries.DoesNotExist:
        return redirect('gestao:index')
        
    if single_review.user == request.user:
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
    
def updategroup(request, group_id):
    try:
        single_group = Groups.objects.get(pk=group_id)
        site_title = f'{single_group.name}'
    except Groups.DoesNotExist:
        return redirect('gestao:index')
    
    if single_group.owner == request.user:
        form_action = reverse('gestao:updategroup', args=(group_id,))

        if request.method == 'POST':
            form = GroupsForm(request.POST, instance=single_group)

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
            'form': GroupsForm(instance=single_group),
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
        
def addwaitlist(request, group_id):
    single_group = Groups.objects.get(pk=group_id)
    user_is_in_waitlist = single_group.waitlist.filter(id=request.user.id).exists()
    if user_is_in_waitlist == False and request.user != single_group.owner:
        single_group.waitlist.add(request.user)
    return redirect('gestao:infogroup', group_id=single_group.pk)

def addmember(request, group_id, user_id):
    single_group = Groups.objects.get(pk=group_id)
    if request.user == single_group.owner:
        user_is_in_group = single_group.members.filter(id=user_id).exists()
        if user_is_in_group == False:
            single_group.members.add(user_id)
            single_group.countmembers += 1
            single_group.waitlist.remove(user_id)
            single_group.save()
    return redirect('gestao:infogroup', group_id=single_group.pk)

def listmovies(request):
    try:

        movies = Movies.objects \
            .order_by('-id') \
            .distinct() 

        context = {
            'create': 'gestao:apimovies',
            'redirect': 'gestao:infomovie',
            'items': movies,
            'site_title': 'Movies'
        }

        return render(
            request,
            'list.html',
            context
        )
    
    except AttributeError:
        context = {
            'site_title': 'Movies'
        }

        return render(
            request,
            'list.html',
            context
        )
    
def listseries(request):
    try:
        series = Series.objects \
        .order_by('-id')\
        .distinct()

        context = {
            'create': 'gestao:apiseries',
            'redirect': 'gestao:infoserie',
            'items': series,
            'site_title': 'Series'
        }

        return render(
            request,
            'list.html',
            context
        )
    
    except AttributeError:
        context = {
            'site_title': 'Series'
        }

        return render(
            request,
            'list.html',
            context
        )
    
def listgroups(request):
    try:
        groups = Groups.objects \
        .order_by('-id')\
        .distinct()

        paginator = Paginator(groups, 6)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        context = {
            'create': 'gestao:creategroup',
            'groups': groups,
            'page_obj': page_obj,
            'site_title': 'Groups'
        }

        return render(
            request,
            'list.html',
            context
        )
    except AttributeError:
        context = {
            'site_title': 'Groups'
        }

        return render(
            request,
            'list.html',
            context
        )
        
    
def deletemovie(request, movie_id):
    if request.user.is_admin:
        single_movie = Movies.objects.get(pk=movie_id)
        single_movie.delete()
    return redirect('gestao:listmovies')
    

def deleteserie(request, serie_id):
    if request.user.is_admin:
        single_serie = Series.objects.get(pk=serie_id)
        single_serie.delete()
    return redirect('gestao:listseries')

def deletenews(request, news_id):
    if request.user.is_admin:
        single_news = News.objects.get(pk=news_id)
        single_news.delete()
    return redirect('gestao:index')


def deletereviewmovie(request, review_id):
    if request.user.is_admin:
        single_review= ReviewsMovies.objects.get(pk=review_id)
        single_review.delete()
    return redirect('gestao:listmovies')

def deletereviewserie(request, review_id):
    if request.user.is_admin:
        single_review = ReviewsSeries.objects.get(pk=review_id)
        single_review.delete()
    return redirect('gestao:listseries')
    
def deletegroup(request, group_id):
    single_group = Groups.objects.get(pk=group_id)
    if single_group.owner == request.user:
        single_group.delete()
        return redirect('gestao:listgroups')
    else:
        return redirect('gestao:listgroups')
    
def removemember(request, user_id, group_id):
    single_group = Groups.objects.get(pk=group_id)
    if single_group.owner == request.user:
        single_group.members.remove(user_id)
        single_group.countmembers += -1
        if single_group.countmembers < 0: 
            single_group.countmembers = 0
        single_group.save()
    return redirect('gestao:infogroup', group_id=single_group.pk)
    
def negarwaitlist(request, group_id, user_id):
    single_group = Groups.objects.get(pk=group_id)
    if request.user == single_group.owner:
        user_is_in_waitlist = single_group.waitlist.filter(id=user_id).exists()
        if user_is_in_waitlist == True:
            single_group.waitlist.remove(user_id)
    return redirect('gestao:infogroup', group_id=single_group.pk)

def infouser(request, user_id):
    try:
        single_user = CustomUser.objects.get(pk=user_id)
    except CustomUser.DoesNotExist:
        return redirect('gestao:index')

    site_title = f'{single_user.username} - '

    context = {
        'user': single_user,
        'site_title': site_title
    }

    return render(
        request,
        'info.html',
        context
    )

def infomovie(request, movie_id):
    try:
        single_movie = Movies.objects.get(pk=movie_id)
    except Movies.DoesNotExist:
        return redirect('gestao:index')
    
    reviews = ReviewsMovies.objects \
        .filter(show=True, movie_id = single_movie)\
        .order_by('-id')

    paginator = Paginator(reviews, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

        
    site_title = f'{single_movie.name} - {single_movie.date.year}'

    context = {
        'grade': single_movie.grade_avg,
        'delete': 'gestao:deletemovie',
        'update': 'gestao:updatemovie',
        'counterlink': 'gestao:inforeviewmovie',
        'titulo': 'REVIEWS',
        'users': reviews,
        'page_obj': page_obj,
        'item': single_movie,
        'site_title': site_title,
        'infoitem': True,
        'create': 'gestao:createreviewmovie',
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
        .filter(show=True, serie_id = single_serie)\
        .order_by('-id')

    paginator = Paginator(reviews, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
        
    site_title = f'{single_serie.name} - {single_serie.date.year}'

    context = {
        'grade': single_serie.grade_avg,
        'delete': 'gestao:deleteserie',
        'update': 'gestao:updateserie',
        'counterlink': 'gestao:inforeviewserie',
        'users': reviews,
        'titulo': 'REVIEWS',
        'page_obj': page_obj,
        'item': single_serie,
        'site_title': site_title,
        'infoitem': True,
        'create': 'gestao:createreviewserie',
    }

    return render(
        request,
        'info.html',
        context
    )

def infonews(request, news_id):
    try:
        single_news = News.objects.get(pk=news_id)
    except News.DoesNotExist:
        return redirect('gestao:index')
    
    site_title = f'{single_news.name} - {single_news.date.day}/{single_news.date.month}'

    context = {
        'news': single_news,
        'site_title': site_title
    }

    return render(
        request,
        'info.html',
        context
    )

def inforeviewmovie(request, review_id):
    try:
        single_review = ReviewsMovies.objects.get(pk=review_id)
    except ReviewsMovies.DoesNotExist:
        return redirect('gestao:index')
    
    site_title = f'{single_review.user} - {single_review.grade}'

    context = {
        'delete': 'gestao:deletereviewmovie',
        'update': 'gestao:updatereviewmovie',
        'Fonte': 'Movie',
        'fonte': single_review.movie,
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
    
    site_title = f'{single_review.user} - {single_review.grade}'

    context = {
        'delete': 'gestao:deletereviewserie',
        'update': 'gestao:updatereviewserie',
        'Fonte': 'Serie',
        'fonte': single_review.serie,
        'review': single_review,
        'site_title': site_title
    }

    return render(
        request,
        'info.html',
        context
    )

def infogroup(request, group_id):
    try:
        single_group = Groups.objects.get(pk=group_id)
    except Groups.DoesNotExist:
        return redirect('gestao:index')

    user_is_in_waitlist = single_group.waitlist.filter(id=request.user.id).exists()   
    user_is_member = single_group.members.filter(id=request.user.id).exists()   

    if request.user == single_group.owner:
        waitlist = CustomUser.objects \
            .filter(waitlist = single_group)\
            .order_by('-id')


        paginator = Paginator(waitlist, 10)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

    else:
        waitlist = None
        page_number = None
        page_obj = None

    site_title = f'{single_group.name}'

    context = {
        'users': waitlist,
        'waitlist': True,
        'titulo': 'WAITLIST',
        'page_obj': page_obj,
        'user_member': user_is_member,
        'user_waitlist': user_is_in_waitlist,
        'group': single_group,
        'site_title': site_title
    }

    return render(
        request,
        'info.html',
        context
    )

def infomembers(request, group_id):
    try:
        single_group = Groups.objects.get(pk=group_id)
    except Groups.DoesNotExist:
        return redirect('gestao:index')
    
    members = CustomUser.objects \
            .filter(members = single_group)\
            .order_by('-id')

    site_title = f'Members of {single_group.name}'

    context = {
        'groups': single_group,
        'members': members,
        'site_title': site_title,
    }

    return render(
        request,
        'info.html',
        context
    )

def infomoviegroup(request, group_id, movie_id):
    try:
        single_group = Groups.objects.get(pk=group_id)
        single_movie = Movies.objects.get(pk=movie_id)
    except Groups.DoesNotExist or Movies.DoesNotExist:
        return redirect('gestao:index')
    
    reviews = ReviewsMovies.objects \
            .filter(movie=movie_id,)\
            .order_by('-id')
    
    members = CustomUser.objects \
            .filter(members = single_group)\
            .order_by('-id') 
    
    contador = 0
    grade = 0

    for review in reviews:
        for member in members:
            if review.user == member:
                grade += review.grade
                contador += 1

    try: 
        grade = grade / contador
    except ZeroDivisionError:
        grade = 'N/A'

    return render(request, 'info.html', {'item': single_movie, 'grade': grade})

def infoseriegroup(request, group_id, serie_id):
    try:
        single_group = Groups.objects.get(pk=group_id)
        single_serie = Series.objects.get(pk=serie_id)
    except Groups.DoesNotExist or Series.DoesNotExist:
        return redirect('gestao:index')
    
    reviews = ReviewsSeries.objects \
            .filter(serie=serie_id,)\
            .order_by('-id')
    
    members = CustomUser.objects \
            .filter(members = single_group)\
            .order_by('-id') 
    
    contador = 0
    grade = 0

    for review in reviews:
        for member in members:
            if review.user == member:
                grade += review.grade
                contador += 1

    try: 
        grade = grade / contador
    except ZeroDivisionError:
        grade = 'N/A'

    return render(request, 'info.html', {'item': single_serie, 'grade': grade})


def apimovies(request):
    form = ApiForm()
    searched = False
    if request.method == 'POST':
        form = ApiForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            year = form.cleaned_data['year']

            if year:
                response = requests.get(f'https://www.omdbapi.com/?t={name}&type=movie&y={year}&apikey={api_key}')
            else:
                response = requests.get(f'https://www.omdbapi.com/?t={name}&type=movie&apikey={api_key}')

            if response.status_code == 200:
                dados_api = response.json()
                name = dados_api.get('Title')
                director = dados_api.get('Director')
                writer = dados_api.get('Writer')
                actors = dados_api.get('Actors')
                poster = dados_api.get('Poster')
                plot = dados_api.get('Plot')
                date = dados_api.get('Released')
                runtime = dados_api.get('Runtime')
                if 'submit_first' in request.POST and name != None:
                    searched = True
                    return render(request, 'register.html', {'form':form, 'api': True, 'apiname': name, 'apidirector': director, 'apiposter': poster, 'apiplot': plot, 'apidate': date, 'apiruntime': runtime, 'searched': searched, 'apiactors': actors, 'apiwriter': writer})
                if 'submit_second' in request.POST:
                    Movies.objects.create(
                        name = dados_api.get('Title'),
                        director = dados_api.get('Director'),
                        writer = dados_api.get('Writer'),
                        poster = dados_api.get('Poster'),
                        actors = dados_api.get('Actors'),
                        plot = dados_api.get('Plot'),
                        date = dados_api.get('Released'),
                        runtime = dados_api.get('Runtime'),
                    )
                    return redirect('gestao:listmovies')
                if 'submit_third' in request.POST:
                    return redirect('gestao:apimovies')
                elif 'submit_fourth' in request.POST:
                    return redirect('gestao:createmovie')

        
    return render(request, 'register.html', {'form':form, 'searched': searched, 'api':True})


def apiseries(request):
    form = ApiForm()
    searched = False
    if request.method == 'POST':
        form = ApiForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            year = form.cleaned_data['year']

            if year:
                response = requests.get(f'https://www.omdbapi.com/?t={name}&type=series&y={year}&apikey={api_key}')
            else:
                response = requests.get(f'https://www.omdbapi.com/?t={name}&type=series&apikey={api_key}')

            if response.status_code == 200:
                dados_api = response.json()
                name = dados_api.get('Title')
                director = dados_api.get('Director')
                writer = dados_api.get('Writer')
                actors = dados_api.get('Actors')
                poster = dados_api.get('Poster')
                plot = dados_api.get('Plot')
                date = dados_api.get('Released')
                seasons = dados_api.get('totalSeasons')
                if 'submit_first' in request.POST and name != None:
                    searched = True
                    return render(request, 'register.html', {'form':form, 'api': True, 'apiname': name, 'apidirector': director, 'apiposter': poster, 'apiplot': plot, 'apidate': date, 'apiseasons': seasons, 'searched': searched, 'apiactors': actors, 'apiwriter': writer})
                elif 'submit_second' in request.POST:
                    Series.objects.create(
                        name = dados_api.get('Title'),
                        director = dados_api.get('Director'),
                        writer = dados_api.get('Writer'),
                        poster = dados_api.get('Poster'),
                        actors = dados_api.get('Actors'),
                        plot = dados_api.get('Plot'),
                        date = dados_api.get('Released'),
                        seasons = dados_api.get('totalSeasons'),
                    )
                    return redirect('gestao:listseries')
                elif 'submit_third' in request.POST:
                    return redirect('gestao:apiseries')
                elif 'submit_fourth' in request.POST:
                    return redirect('gestao:createserie')

        
    return render(request, 'register.html', {'form':form, 'searched': searched, 'api':True})