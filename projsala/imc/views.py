from django.shortcuts import render
from django.http import HttpResponse
from .services import IMCService
# Create your views here.​

def index(request):
    return render(request,'index.html')
def nome(request):
    return HttpResponse("<h1>André Gustavo Duarte</h1>")
def calcular_imc(request):
    altura = float(request.POST.get('altura'))
    peso = float(request.POST.get('peso'))
    imc, classificacao = IMCService.calcular_imc(peso, altura)
    contexto= {
        'imc': imc,
        'classificacao': classificacao,
        'altura': altura,
        'peso': peso,
    }
    return render(request, 'resultado_imc.html', contexto)
def tabuada(request, numero):
    html=f'<table border="1"><tr><td>Tabuada de {numero}</td></tr>'
    for i in range(1,11):
        html+=f'<tr><td>{i} x {numero} = {i*numero}</td></tr>'
    html+='</table>'
    return HttpResponse(html)