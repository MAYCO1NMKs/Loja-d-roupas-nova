from django import forms
from .models import Pedido

class FormularioPedido(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = [] # Nenhum campo do modelo Pedido será exibido diretamente

    # Campos adicionais para o formulário de checkout
    nome_completo = forms.CharField(max_length=100, label="Nome Completo", 
                              widget=forms.TextInput(attrs={'placeholder': 'Seu nome completo'}))
    email = forms.EmailField(label="E-mail",
                         widget=forms.EmailInput(attrs={'placeholder': 'seuemail@exemplo.com'}))
    endereco_linha_1 = forms.CharField(max_length=255, label="Endereço",
                                 widget=forms.TextInput(attrs={'placeholder': 'Rua, número e complemento'}))
    cidade = forms.CharField(max_length=100, label="Cidade", 
                         widget=forms.TextInput(attrs={'placeholder': 'Sua cidade'}))
    estado = forms.CharField(max_length=100, label="Estado", 
                       widget=forms.TextInput(attrs={'placeholder': 'Seu estado'}))
    cep = forms.CharField(max_length=9, label="CEP", 
                    widget=forms.TextInput(attrs={'placeholder': 'XXXXX-XXX'}))
