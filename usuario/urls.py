from django.urls import path
from . import views

app_name = "usuario"

urlpatterns = [
    path("perfil/", views.profile_view, name="perfil"),
    path("perfil/editar/", views.editar_perfil, name="editar_perfil"),
]
