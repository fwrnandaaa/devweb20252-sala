from django.shortcuts import render
from .services import  EnqueteService
# Create your views here.

enquete = EnqueteService.criar_enquete()


def home(request):
    contexto={'pergunta':enquete.pergunta.texto,
              'alternativa1':enquete.pergunta.opcoes[0].texto,
              'alternativa2':enquete.pergunta.opcoes[1].texto,
              'alternativa3':enquete.pergunta.opcoes[2].texto,
              'alternativa4':enquete.pergunta.opcoes[3].texto}
    return render(request,'enquete/index.html',contexto)
def votar(request):
    
    alternativa=request.POST.get('alternativa')
    EnqueteService.registrar_voto(enquete, alternativa)

    contexto={'pergunta':enquete.pergunta.texto,
              'alternativa1':enquete.pergunta.opcoes[0].texto,
              'alternativa2':enquete.pergunta.opcoes[1].texto,
              'alternativa3':enquete.pergunta.opcoes[2].texto,
              'alternativa4':enquete.pergunta.opcoes[3].texto,
              'voto1':enquete.pergunta.opcoes[0].votos,
              'voto2':enquete.pergunta.opcoes[1].votos,
              'voto3':enquete.pergunta.opcoes[2].votos,
              'voto4':enquete.pergunta.opcoes[3].votos,
              'total_votos':enquete.pergunta.total_votos()}
    return render(request,'enquete/resultado.html',contexto)