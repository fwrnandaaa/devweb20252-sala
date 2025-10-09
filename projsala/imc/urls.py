from django.urls import path

from . import views
app_name="imc"
urlpatterns=[
    path('',views.index,name='index'),
    path('nome/',views.nome,name='nome'),
    path('tabuada/<int:numero>/',views.tabuada,name='tabuada'),
    path("calcular/", views.calcular_imc, name="calcular_imc" ),
    #path('calcular/<int:altura>/<int:peso>/',views.calcular_imc,name='calcular_imc')
]