# pedidos/forms.py
from django import forms
from .models import Pedido

class CheckoutForm(forms.ModelForm):
    METODO_PAGAMENTO_CHOICES = (
        ('pix', 'Pix'),
        ('cartao', 'Cartão de Crédito/Débito'),
    )

    metodo_pagamento = forms.ChoiceField(
        choices=METODO_PAGAMENTO_CHOICES,
        widget=forms.RadioSelect, # Para aparecer como botões de rádio
        label="Método de Pagamento"
    )

    class Meta:
        model = Pedido
        fields = ['nome_cliente', 'email_cliente', 'telefone_cliente', 'metodo_pagamento']
        labels = {
            'nome_cliente': 'Nome Completo',
            'email_cliente': 'E-mail',
            'telefone_cliente': 'Telefone (com DDD)',
        }
        widgets = {
            'nome_cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'email_cliente': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefone_cliente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(XX) XXXXX-XXXX'}),
        }
