
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import UserProfileForm


@login_required
def profile_view(request):
    """Exibe a página de perfil do usuário logado."""
    context = {"user": request.user}
    return render(request, "usuario/perfil.html", context)


@login_required
def editar_perfil(request):
    """Permite que o usuário edite suas informações de perfil."""
    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Seu perfil foi atualizado com sucesso!")
            return redirect("usuario:profile_view")
    else:
        form = UserProfileForm(instance=request.user)

    context = {"form": form}
    return render(request, "usuario/editar_perfil.html", context)
