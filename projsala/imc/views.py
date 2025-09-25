from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.​

def index(request):
    return HttpResponse("<h1> Bem-vindo(a) à aplicação IMC</h1>")
def nome(request):
    return HttpResponse("<h1>André Gustavo Duarte</h1>")
def tabuada_tres(request):
    html='<table border="1"><tr><td>Tabuada de três</td></tr>'
    for i in range(1,11):
        html+=f'<tr><td>{i} x 3 = {i*3}</td></tr>'
    html+='</table>'
    return HttpResponse(html)