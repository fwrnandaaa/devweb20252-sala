from django.urls import path

from . import views
app_name='enquete'
urlpatterns=[
    path('',views.home,name='index'),
    path('votar/',views.votar,name='votar'),
]