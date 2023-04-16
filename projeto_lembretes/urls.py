"""
URL configuration for projeto_lembretes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from lembretes.views import lista_lembrete, criando_lembrete, remover_lembrete

urlpatterns = [
    path('lista_lembrete/', lista_lembrete, name='lista_lembrete'),
    path('lista_lembrete/criar_lembrete/', criando_lembrete, name='criando_lembrete'),
    path('remover/<int:id>', remover_lembrete, name='remover_lembrete'),
    path('admin/', admin.site.urls),
]
