from django.urls import path
from . import views

urlpatterns = [
    path('carrinho/', views.carrinho, name='carrinho'),
]
