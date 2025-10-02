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
    #Lógica para contabilizar votos
    render(request,'resultado.html')