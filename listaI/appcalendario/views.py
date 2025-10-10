from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

def index(request):
    """
    View principal que exibe o formulário do calendário
    """
    return render(request, 'index.html')


@csrf_exempt
def gerar_calendario(request):
    dias_selecionados = request.POST.getlist('dias')
    materias_por_dia = [[] for _ in dias_selecionados]
    materias = request.POST.get('materias', '')
    lista_materias = [m.strip() for m in materias.split(',') if m.strip()]
    contador_dias=0
    for materia in lista_materias:
        materias_por_dia[contador_dias].append(materia)
        contador_dias+=1
        if contador_dias >= len(dias_selecionados):
            contador_dias = 0
    contexto={
        'dias': dias_selecionados,
        'materias_por_dia': materias_por_dia,
    }
    return render(request, 'resultado.html', contexto)



            
            

