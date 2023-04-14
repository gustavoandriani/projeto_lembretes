from django.shortcuts import render, redirect
from .models import lembrete
from .forms import criar_lembrete
# Create your views here.

def lista_lembrete(request):
    lembretes = lembrete.objects.all()
    return render(request, 'lista_lembrete.html', {'lembretes': lembretes})

def criando_lembrete(request):
    if request.method == 'POST':
        form = criar_lembrete(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
    else:
        form = criar_lembrete()
    return render(request, 'criar_lembrete.html', {'form': form})