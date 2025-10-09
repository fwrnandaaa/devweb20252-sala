from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.​

def index(request):
    return render(request,'index.html')
def nome(request):
    return HttpResponse("<h1>André Gustavo Duarte</h1>")
def calcular_imc(request):
    altura = float(request.POST.get('altura'))
    peso = float(request.POST.get('peso'))
    imc= peso/(altura*altura)
    if imc < 18.5:
        classificacao = 'Abaixo do peso'
    elif imc < 24.9:
        classificacao = 'Peso normal'
    elif imc < 29.9:
        classificacao = 'Sobrepeso'
    else:
        classificacao = 'Obesidade'
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