from django.shortcuts import render, redirect
from .models import lembrete
from .forms import criar_lembrete
# Create your views here.

def lista_lembrete(request):
    lembretes = lembrete.objects.all()
    total_lembretes = lembrete.objects.count()
    return render(request, 'lista_lembrete.html', {'lembretes': lembretes, 'total_lembretes': total_lembretes})


def criando_lembrete(request):
    if request.method == 'POST':
        form = criar_lembrete(request.POST)
        if form.is_valid():
            form.save()
            return redirect('criando_lembrete')
    else:
        form = criar_lembrete()
    return render(request, 'criar_lembrete.html', {'form': form})

def remover_lembrete(request, id):
    removerLembrete = lembrete.objects.get(id=id)
    lembrete.delete(removerLembrete)
    return redirect('lista_lembrete')