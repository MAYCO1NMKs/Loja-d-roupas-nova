from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

# Formulário de Cadastro personalizado.
class CustomUserCreationForm(UserCreationForm):
    image_profile = forms.ImageField(required=False, label="Foto de Perfil")

    class Meta:
        model = User
        fields = ('username', 'email', 'image_profile',)

# Formulário de Login personalizado e moderno.
class CustomAuthenticationForm(AuthenticationForm):
    # Adiciona o campo "Lembrar-me"
    remember_me = forms.BooleanField(required=False, initial=True, label="Lembrar-me")

    def __init__(self, *args, **kwargs):
        super(CustomAuthenticationForm, self).__init__(*args, **kwargs)
        # Adiciona placeholders e classes CSS para um visual moderno
        self.fields['username'].widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Nome de utilizador',
                'id': 'floatingInput',
            }
        )
        self.fields['password'].widget = forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Palavra-passe',
                'id': 'floatingPassword',
            }
        )
