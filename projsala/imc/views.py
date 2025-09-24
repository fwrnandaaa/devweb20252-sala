from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.​

def index(request):
    return HttpResponse("<h1> Bem-vindo(a) à aplicação IMC</h1>")
def nome(request):
    return HttpResponse("<h1>André Gustavo Duarte</h1>")