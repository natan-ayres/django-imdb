from gestao.models import User, Filmes, Reviews
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import password_validation

class FilmesForm(forms.ModelForm):
    nome = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Nome',
                'class': ''
            }
        )
    )

    class Meta:
        model = Filmes
        fields = (
            'nome', 'desc', 'data', 'foto'
        )

class ReviewForm(forms.ModelForm):
    filme = forms.ModelChoiceField(
        queryset=Filmes.objects.all(),
        label='Filme',
        required=True
    )
    nota = forms.FloatField(
        label='Nota',
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
        model = Reviews
        fields = (
            'filme', 'review', 'nota'
        )

    def __init__(self, *args, **kwargs):
        usuario = kwargs.pop('usuario')
        super().__init__(*args, **kwargs)
        filmes_avaliados = Filmes.objects.filter(avaliacoes=usuario)
        self.fields['filme'].queryset = Filmes.objects.exclude(id__in=filmes_avaliados)

class RegisterForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Usuário',
                'class': 'inputlogin',
            }
        ),
        label = 'Usuário',
        required=True,
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Senha',
                'class': 'inputlogin',
            }
        ),
        label = 'Senha',
        required=True,
        help_text= 'Acima de 8 dígitos'
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Digite novamente',
                'class': 'inputlogin',
            }
        ),
        label = 'Confirme a senha' ,
        required=True,
    )


    class Meta:
        model = User
        fields = (
            'username', 'password1', 'password2',
        )



class RegisterUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email', 'username', 'password1', 'password2',
        )
    
    first_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        error_messages={
            'min_length': 'Porfavor, acima de 2 digitos.',
            'max_length': 'Porfavor, abaixo de 30 digitos.'
        },
    )
    last_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        error_messages={
            'min_length': 'Porfavor, acima de 2 digitos.',
            'max_length': 'Porfavor, abaixo de 30 digitos.'
        },
    )
    password1 = forms.CharField(
        label='Senha',
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        required=False
    )
    password2 = forms.CharField(
        label='Confirme a senha',
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        required=False
    )



    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email != self.instance.email:
            if User.objects.filter(email=email).exists():
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
            'placeholder': 'Nome',
            'aria-describedby': 'usernameHelp'
        }),
    )
    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={
            'class': 'inputlogin',
            'placeholder': 'Senha',
            'aria-describedby': 'passwordHelp'
        }),
    )