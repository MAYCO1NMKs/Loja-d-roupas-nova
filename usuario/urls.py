from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('cadastro/', views.cadastro_view, name='cadastro'),

    path('gerenciar-produtos/', views.gerenciar_produtos, name='gerenciar_produtos'),
    path('ver-contas/', views.ver_contas, name='ver_contas'),
    path('carrinho/', views.carrinho, name='carrinho'),
    path('perfil/', views.editar_perfil, name='perfil'),
]
