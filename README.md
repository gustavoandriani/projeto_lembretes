# Projeto Lembretes

<div id="inicio"></div>

Este é um projeto desenvolvido para estudos, nele, utilizei HTML, CSS, JavaScript e Python/Django.
A ideia principal é a criação simples de lembretes para os usuários. Por enquanto não existe uma sessão de login/cadastro para eu poder deixar essa ferramenta online. Então logo abaixo deixarei caminhos para você poder rodar na sua máquina.

<strong>
<ul>
  <li>
    <a href="#sobre">Sobre</a>
  </li>
  <li>
    <a href="#tutorial">Tutorial</a>
  </li>
</ul>
</strong>


## Explicando sobre

<div id="sobre"></div>

- Dentro do arquivo localizado em "lembretes/models.py" você encontrará as predefinições necessárias para o banco de dados da ferramenta.

```
  from django.db import models

  # Create your models here.
  class lembrete(models.Model):
      title = models.CharField(max_length=200)
      text = models.TextField()
```

- Em "lembretes/views.py" terá todas as funções necessárias para criar e remover lembretes.

```
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
```

- No diretório "lembretes/forms.py" é configurado o padrão do formulário de criação de lembretes

```
  from django import forms
  from .models import lembrete

  class criar_lembrete(forms.ModelForm):
      class Meta:
          model = lembrete
          fields = ['title', 'text']
```

- Em "projeto_lembretes/urls.py" temos a configuração de acesso de todas as páginas.(Se você acessar o diretório "lembretes/urls.py" irá encontrar um padrão de diretório que utilizei no início do projeto, porém, com os ajustes achei melhor deixar todos no diretório principal do projeto.)

```
  from django.contrib import admin
  from django.urls import path
  from lembretes.views import lista_lembrete, criando_lembrete, remover_lembrete

  urlpatterns = [
      path('lista_lembrete/', lista_lembrete, name='lista_lembrete'),
      path('lista_lembrete/criar_lembrete/', criando_lembrete, name='criando_lembrete'),
      path('remover/<int:id>', remover_lembrete, name='remover_lembrete'),
      path('admin/', admin.site.urls),
  ]
```

- Para acessar os templates das páginas HTML basta ir no diretório "lembretes/templates". E para acessar os arquivos estáticos do projeto o diretório é "lembretes/static/lembretes".

## Como clonar e rodar o projeto

<div id="tutorial"></div>

O primeiro passo é ter o Python e o Git instalados em sua máquina.

<strong>
<a style="background-color: white; padding: 3px; color: black;" href="https://git-scm.com/">Baixar Git</a>
<a style="background-color: white; padding: 3px; color: black;" href="https://www.python.org/">Baixar Python</a>
</strong>

A seguir, abra um terminal de comandos e navegue até o diretório que queira clonar o repositório usando o comando:

```
  cd [diretório_de_destino]
  
  Exemplo:
  cd ~/Documents
```

Após isso use o comando Git para clonar o projeto:

```
  git clone https://github.com/gustavoandriani/projeto_lembretes.git
```

Pressione "ENTER" e o Git fará o download de todos os arquivos para o diretório.

Agora, abra um terminal na raiz do projeto clonado e utilize o comando:

```
  python manage.py runserver
```

Ao pressionar "ENTER" o python começará a rodar a aplicação, para poder acessar basta apenas clicar no atalho localizado dentro da raiz do projeto com o nome de "WebApp.url".