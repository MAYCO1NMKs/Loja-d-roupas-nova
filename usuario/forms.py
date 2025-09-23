from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

# Formulário de Cadastro personalizado.
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')

# Formulário de Login personalizado e moderno.
class CustomAuthenticationForm(AuthenticationForm):
    remember_me = forms.BooleanField(required=False, initial=True, label="Lembrar-me")

    def __init__(self, *args, **kwargs):
        super(CustomAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Nome de utilizador'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Palavra-passe'})

# Formulário para editar o perfil completo do usuário
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'foto_perfil', 'first_name', 'last_name', 'email', 'telefone',
            'cep', 'endereco', 'numero', 'complemento', 'bairro', 'cidade', 'estado'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Seu nome'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Seu sobrenome'}),
            'email': forms.EmailInput(attrs={'placeholder': 'seu@email.com'}),
            'telefone': forms.TextInput(attrs={'placeholder': '(XX) XXXXX-XXXX'}),
            'cep': forms.TextInput(attrs={'placeholder': '00000-000'}),
            'endereco': forms.TextInput(attrs={'placeholder': 'Rua, Avenida, etc.'}),
            'numero': forms.TextInput(attrs={'placeholder': 'Nº'}),
            'complemento': forms.TextInput(attrs={'placeholder': 'Apto, Bloco, Casa'}),
            'bairro': forms.TextInput(attrs={'placeholder': 'Seu bairro'}),
            'cidade': forms.TextInput(attrs={'placeholder': 'Sua cidade'}),
            'estado': forms.TextInput(attrs={'placeholder': 'UF', 'maxlength': '2'}),
        }
