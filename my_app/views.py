from django.shortcuts import render
from .forms import *


def cadastrar_usuario(request):
    form = UsuarioForm()
    return render(request, "form.html", {'form': form})
