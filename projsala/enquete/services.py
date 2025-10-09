class Pergunta:
    def __init__(self,texto):
        self.texto=texto
        self.opcoes=[]
    def adicionar_opcao(self,opcao):
        self.opcoes.append(opcao)
    def total_votos(self):
        return sum(opcao.votos for opcao in self.opcoes)
class Opcoes:
    def __init__(self,texto):
        self.texto=texto
        self.votos=0
    def votar(self):
        self.votos+=1
class Enquete:
    def __init__(self,pergunta):
        self.pergunta=pergunta
    def votar(self,opcao_texto):
        for opcao in self.pergunta.opcoes:
            if opcao.texto == opcao_texto:
                opcao.votar()
                return True
        return False

class EnqueteService:
    @staticmethod
    def criar_enquete():
        pergunta = Pergunta("Qual seu animal favorito?")
        pergunta.adicionar_opcao(Opcoes("Cachorro"))
        pergunta.adicionar_opcao(Opcoes("Gato"))
        pergunta.adicionar_opcao(Opcoes("Pássaro"))
        pergunta.adicionar_opcao(Opcoes("Peixe"))
        return Enquete(pergunta)
    @staticmethod
    def registrar_voto(enquete,opcao_texto):
        return enquete.votar(opcao_texto)