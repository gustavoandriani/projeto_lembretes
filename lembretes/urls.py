from django.urls import path
from lembretes import views

urlpatterns = [
    path('', views.lista_lembrete, name='lista_lembrete'),
    path('', views.criando_lembrete, name='criar_lembrete'),
]
