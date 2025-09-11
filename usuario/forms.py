from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

# Formulário de Cadastro personalizado.
# Ele herda de `UserCreationForm` para já ter os campos básicos de usuário.
class CustomUserCreationForm(UserCreationForm):
    # O campo `image_profile` é adicionado aqui para que o formulário
    # possa manipulá-lo. O `required=False` permite que o usuário não
    # selecione uma foto, usando a imagem padrão.
    image_profile = forms.ImageField(required=False, label="Foto de Perfil")

    class Meta:
        # A classe Meta diz ao formulário qual modelo ele deve usar.
        model = User
        # Definimos os campos que queremos no formulário de cadastro.
        fields = ('username', 'email', 'image_profile',)

# Formulário de Login.
# Usamos `AuthenticationForm` para lidar com a autenticação de forma segura.
class CustomAuthenticationForm(AuthenticationForm):
    # O Django já lida com os campos `username` e `password` de forma segura.
    pass
