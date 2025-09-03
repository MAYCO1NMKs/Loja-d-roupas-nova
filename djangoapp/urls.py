from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuario/', include('usuario.urls')),  
    path('', lambda request: redirect('login')), 
]

