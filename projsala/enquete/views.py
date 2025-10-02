from django.shortcuts import render

# Create your views here.

pergunta="Qual seu animal favorito?"
alternativa1="Cachorro"
alternativa2="Gato"
alternativa3="Pássaro"
alternativa4="Peixe"
voto1=0
voto2=0
voto3=0
voto4=0
def home(request):
    contexto={'pergunta':pergunta,
              'alternativa1':alternativa1,
              'alternativa2':alternativa2,
              'alternativa3':alternativa3,
              'alternativa4':alternativa4}
    return render(request,'home.html',contexto)
def votar(request):
    global voto1,voto2,voto3,voto4
    alternativa=request.GET.get('alternativa')
    if alternativa==alternativa1:
        voto1+=1
    elif alternativa==alternativa2:
        voto2+=1
    elif alternativa==alternativa3:
        voto3+=1
    elif alternativa==alternativa4:
        voto4+=1
    total_votos=voto1+voto2+voto3+voto4
    contexto={'pergunta':pergunta,
              'alternativa1':alternativa1,
              'alternativa2':alternativa2,
              'alternativa3':alternativa3,
              'alternativa4':alternativa4,
              'voto1':voto1,
              'voto2':voto2,
              'voto3':voto3,
              'voto4':voto4,
              'total_votos':total_votos}
    return render(request,'resultado.html',contexto)