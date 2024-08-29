from gestao.models import CustomUser, Movies, ReviewsMovies, News, Series, ReviewsSeries, Groups
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth import password_validation

class NewsForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Title'
            }
        )
    )
    text = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder': 'News'
            }
        )
    )
    class Meta:
        model = News
        fields = [
            'name', 'text', 'image'
        ]

class MoviesForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Name',
                'class': ''
            }
        )
    )

    director = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Director',
                'class': ''
            }
        )
    )

    plot = forms.CharField(
        label='Plot', widget=forms.Textarea(
            attrs={
                'placeholder': 'Plot',
                'class': ''
            }
        ), required=False
    )
    date = forms.DateField(
        label='Data',widget=forms.DateInput(
            attrs={
                'type': 'date'
            }
        ), required=True
    )
    runtime = forms.TimeField(
        label='Runtime', widget=forms.TimeInput(
            attrs={
                'type': 'time'
            }
        )
    )

    class Meta:
        model = Movies
        fields = (
            'name', 'director', 'rating', 'runtime', 'plot', 'writer', 'actors', 'date', 'poster'
        )

class ReviewMovieForm(forms.ModelForm):
    movie = forms.ModelChoiceField(
        queryset=Movies.objects.all(),
        label='Movie',
        required=True
    )
    grade = forms.FloatField(
        label='Grade',
        required=True,
        validators=[MinValueValidator(0,0), MaxValueValidator(10,0)]
    )
    review = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Review',
            }
        ),
        label='Review',
        required=False
    )

    class Meta:
        model = ReviewsMovies
        fields = (
            'movie', 'review', 'grade'
        )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        movies_reviewds = Movies.objects.filter(reviews=user)
        self.fields['movie'].queryset = Movies.objects.exclude(id__in=movies_reviewds)

class ReviewUpdateMovieForm(forms.ModelForm):
    movie = forms.ModelChoiceField(
        queryset=Movies.objects.all(),
        label='Movie',
        required=True
    )
    grade = forms.FloatField(
        label='Grade',
        required=True,
        validators=[MinValueValidator(0,0), MaxValueValidator(10,0)]
    )
    review = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Review',
            }
        ),
        label='Review',
        required=False
    )

    class Meta:
        model = ReviewsMovies
        fields = (
            'movie', 'review', 'grade'
        )

class ReviewSeriesForm(forms.ModelForm):
    serie = forms.ModelChoiceField(
        queryset=Series.objects.all(),
        label='Serie',
        required=True
    )
    grade = forms.FloatField(
        label='Grade',
        required=True,
        validators=[MinValueValidator(0,0), MaxValueValidator(10,0)]
    )
    review = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Review',
            }
        ),
        label='Review',
        required=False
    )

    class Meta:
        model = ReviewsSeries
        fields = (
            'serie', 'review', 'grade'
        )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        series_reviewds = Series.objects.filter(reviews=user)
        self.fields['serie'].queryset = Series.objects.exclude(id__in=series_reviewds)

class ReviewUpdateSeriesForm(forms.ModelForm):
    serie = forms.ModelChoiceField(
        queryset=Series.objects.all(),
        label='Serie',
        required=True
    )
    grade = forms.FloatField(
        label='Grade',
        required=True,
        validators=[MinValueValidator(0,0), MaxValueValidator(10,0)]
    )
    review = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Review',
            }
        ),
        label='Review',
        required=False
    )

    class Meta:
        model = ReviewsSeries
        fields = (
            'serie', 'review', 'grade'
        )

class SeriesForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Name',
                'class': ''
            }
        )
    )

    director = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Director',
                'class': ''
            }
        ),required=False
    )
    date = forms.DateField(
        label='Started',widget=forms.DateInput(
            attrs={
                'type': 'date'
            }
        ), required=True
    )
    date_end = forms.DateField(
        label='Ending',widget=forms.DateInput(
            attrs={
                'type': 'date'
            }
        ), required=False
    )
    episodes = forms.IntegerField(
        label='Episodes', widget=forms.NumberInput()
    )
    seasons = forms.IntegerField(
        label='Seasons', widget=forms.NumberInput()
    )
    plot = forms.CharField(
        label='Plot', widget=forms.Textarea(
            attrs={
                'placeholder': 'Plot',
                'class': ''
            }
        ), required=False
    )

    class Meta:
        model = Series
        fields = (
            'name', 'director', 'date', 'date_end', 'episodes', 'actors', 'writer', 'rating','seasons', 'plot', 'poster'
        )

class GroupsForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Name',
                'class': ''
            }
        )
    )
    desc = forms.CharField(
        label='Description', widget=forms.Textarea(
            attrs={
                'placeholder': 'Description',
                'class': ''
            }
        ), required=False
    )


    class Meta:
        model = Groups
        fields = (
            'name', 'desc', 'image'
        )

class RegisterForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Username',
                'class': 'inputlogin',
            }
        ),
        label = 'Username',
        required=True,
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password',
                'class': 'inputlogin',
            }
        ),
        label = 'Password',
        required=True,
        help_text= 'Above 8 digits'
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Confirm',
                'class': 'inputlogin',
            }
        ),
        label = 'Confirm your password' ,
        required=True,
    )


    class Meta:
        model = CustomUser
        fields = (
            'username', 'password1', 'password2',
        )



class RegisterUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = (
            'first_name', 'last_name', 'email', 'username', 'password1', 'password2',
        )
    
    first_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        error_messages={
            'min_length': 'Please, above 2 digits',
            'max_length': 'Please, below 30 digits'
        },
    )
    last_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        error_messages={
            'min_length': 'Please, above 2 digits',
            'max_length': 'Please, below 30 digits'
        },
    )
    password1 = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        required=False
    )
    password2 = forms.CharField(
        label='Confirm the Password',
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        required=False
    )



    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email != self.instance.email:
            if CustomUser.objects.filter(email=email).exists():
                self.add_error(
                    'email',
                    ValidationError('This email already exists', code='invalid')
                )
            else:
                return email
        return email
    
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if password1:
            try:
                password_validation.validate_password(password1)
            except ValidationError as errors:
                self.add_error(
                    'password1',
                    ValidationError(errors)
                )
    
    def clean_password2(self):
        password2 = self.cleaned_data.get('password2')

        if password2:
            try:
                password_validation.validate_password(password2)
            except ValidationError as errors:
                self.add_error(
                    'password2',
                    ValidationError(errors)
                )
    
    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        user = super().save(commit=False)
        password = cleaned_data.get('password1')

        if password:
            user.set_password(password)

        if commit:
            user.save()

    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 or password2:
            if password1 != password2:
                self.add_error(
                    'password2',
                    ValidationError('Passwords do not match', code='invalid')
                )
        return super().clean()
    
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'inputlogin',
            'placeholder': 'Name',
            'aria-describedby': 'usernameHelp'
        }),
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'class': 'inputlogin',
            'placeholder': 'Password',
            'aria-describedby': 'passwordHelp'
        }),
    )

class ApiForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Name',
                'class': ''
            }
        )
    )
    year = forms.IntegerField(
        label="Year",
        min_value=1900,  
        max_value=2024,  
        required=False,
    )

