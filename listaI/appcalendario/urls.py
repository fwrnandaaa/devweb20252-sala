from django.urls import path
from . import views

app_name = 'appcalendario'

urlpatterns = [
    # Página principal do calendário
    path('', views.index, name='index'),
    # URL para processar o formulário
    path('calendario/', views.gerar_calendario, name='gerar_calendario'),
]