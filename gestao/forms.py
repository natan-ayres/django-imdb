from gestao.models import CustomUser, Filmes, ReviewsFilmes, Noticias, Series, ReviewsSeries, Grupos
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth import password_validation

class NoticiasForm(forms.ModelForm):
    nome = forms.CharField(
        label='Title',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Title'
            }
        )
    )
    texto = forms.CharField(
        label='Info',
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Information'
            }
        )
    )
    imagem = forms.ImageField(
        label='Image'
    )
    class Meta:
        model = Noticias
        fields = [
            'nome', 'texto', 'imagem'
        ]

class FilmesForm(forms.ModelForm):
    nome = forms.CharField(
        label='Name',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Name',
                'class': ''
            }
        )
    )

    diretor = forms.CharField(
        label='Director',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Director',
                'class': ''
            }
        )
    )

    sinopse = forms.CharField(
        label='Plot', widget=forms.Textarea(
            attrs={
                'placeholder': 'Plot',
                'class': ''
            }
        ), required=False
    )
    data = forms.DateField(
        label='Date',widget=forms.DateInput(
            attrs={
                'type': 'date'
            }
        ), required=True
    )
    duracao = forms.TimeField(
        label='Runtime', widget=forms.TimeInput(
            attrs={
                'type': 'time'
            }
        )
    )

    class Meta:
        model = Filmes
        fields = (
            'nome', 'diretor', 'classificacao', 'duracao', 'sinopse', 'escritor', 'atores', 'data', 'poster'
        )

class ReviewFilmeForm(forms.ModelForm):
    filme = forms.ModelChoiceField(
        queryset=Filmes.objects.all(),
        label='Movie',
        required=True
    )
    nota = forms.FloatField(
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
        model = ReviewsFilmes
        fields = (
            'filme', 'review', 'nota'
        )

    def __init__(self, *args, **kwargs):
        usuario = kwargs.pop('usuario')
        super().__init__(*args, **kwargs)
        filmes_avaliados = Filmes.objects.filter(avaliacoes=usuario)
        self.fields['filme'].queryset = Filmes.objects.exclude(id__in=filmes_avaliados)

class ReviewFilmeFiltroForm(forms.ModelForm):
    nota = forms.FloatField(
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
        model = ReviewsFilmes
        fields = (
            'review', 'nota'
        )

class ReviewSerieFiltroForm(forms.ModelForm):
    nota = forms.FloatField(
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
            'review', 'nota'
        )

class ReviewUpdateFilmeForm(forms.ModelForm):
    filme = forms.ModelChoiceField(
        queryset=Filmes.objects.all(),
        label='Movie',
        required=True
    )
    nota = forms.FloatField(
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
        model = ReviewsFilmes
        fields = (
            'filme', 'review', 'nota'
        )

class ReviewSeriesForm(forms.ModelForm):
    serie = forms.ModelChoiceField(
        queryset=Series.objects.all(),
        label='Serie',
        required=True
    )
    nota = forms.FloatField(
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
            'serie', 'review', 'nota'
        )

    def __init__(self, *args, **kwargs):
        usuario = kwargs.pop('usuario')
        super().__init__(*args, **kwargs)
        series_avaliadas = Series.objects.filter(avaliacoes=usuario)
        self.fields['serie'].queryset = Series.objects.exclude(id__in=series_avaliadas)

class ReviewUpdateSeriesForm(forms.ModelForm):
    serie = forms.ModelChoiceField(
        queryset=Series.objects.all(),
        label='Serie',
        required=True
    )
    nota = forms.FloatField(
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
            'serie', 'review', 'nota'
        )

class SeriesForm(forms.ModelForm):
    nome = forms.CharField(
        label='Name',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Name',
                'class': ''
            }
        )
    )

    diretor = forms.CharField(
        label='Director',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Director',
                'class': ''
            }
        ),required=False
    )
    data = forms.DateField(
        label='Start Date',widget=forms.DateInput(
            attrs={
                'type': 'date'
            }
        ), required=True
    )
    data_termino = forms.DateField(
        label='End Date',widget=forms.DateInput(
            attrs={
                'type': 'date'
            }
        ), required=False
    )
    episodios = forms.IntegerField(
        label='Episodes', widget=forms.NumberInput()
    )
    temporadas = forms.IntegerField(
        label='Seasons', widget=forms.NumberInput()
    )
    sinopse = forms.CharField(
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
            'nome', 'diretor', 'data', 'data_termino', 'episodios', 'atores', 'escritor', 'classificacao','temporadas', 'sinopse', 'poster'
        )

class GruposForm(forms.ModelForm):
    nome = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Name',
                'class': ''
            }
        ),
        label='Name'
    )
    desc = forms.CharField(
        label='Description', widget=forms.Textarea(
            attrs={
                'placeholder': 'Description',
                'class': ''
            }
        ), required=False
    )
    imagem = forms.ImageField(
        label='Image'
    )


    class Meta:
        model = Grupos
        fields = (
            'nome', 'desc', 'imagem'
        )

class RegisterForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Username',
                'class': 'inputlogin',
            }
        ),
        required=True,
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password',
                'class': 'inputlogin',
            }
        ),
        required=True,
        help_text= 'Above 8 digits!'
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Confirm your Password',
                'class': 'inputlogin',
            }
        ),
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
            'min_length': 'Please, above 2 digits.',
            'max_length': 'Please, below 30 digits.'
        },
    )
    last_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        error_messages={
            'min_length': 'Please, above 2 digits.',
            'max_length': 'Please, below 30 digits.'
        },
    )
    password1 = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        required=False
    )
    password2 = forms.CharField(
        label='Confirm Password',
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
                    ValidationError('Já existe este e-mail', code='invalid')
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
                    ValidationError('Senhas não batem', code='invalid')
                )
        return super().clean()
    
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'inputlogin',
            'placeholder': 'Username',
            'aria-describedby': 'usernameHelp'
        }),
    )
    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={
            'class': 'inputlogin',
            'placeholder': 'Password',
            'aria-describedby': 'passwordHelp'
        }),
    )

class ApiForm(forms.Form):
    nome = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Name',
                'class': ''
            }
        ),
        label='Name'
    )
    ano = forms.IntegerField(
        label="Year",
        min_value=1900,  
        max_value=2024,  
        required=False,
    )

