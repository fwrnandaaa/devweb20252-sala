from django.urls import path

from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('nome/',views.nome,name='nome'),
    path('tabuada/tres/',views.tabuada_tres,name='tabuada_tres'),
]