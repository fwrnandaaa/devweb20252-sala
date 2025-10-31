from django.db import models

# Create your models here.
class Raca(models.Model): #fazendo herança a partir da classe model
    nome=models.CharField(max_length=100,unique=True) #models.charfield= chama construtor e passa 2 parametros: max_length e unique; o que quer dizer que só é possivel cadastrar uma raça com no max 100 caracteres e ele deve ser unique

class Gato(models.Model):
    #max_length define o tamanho maximo do atributo
    #choices = define os valores possiveis para o atributo 'sexo'; palavra completa é o que aparece para o usuário e a letra inicial fica salvo no bd
    #TextField = Campo de texto longo
    #Blank = True quer dizer que permite que o formulário seja enviado com o campo 'descricao' em branco
    nome=models.CharField(max_length=100)
    sexo=models.CharField(max_length=1,choices=[('M','Macho'),('F','Femea')])
    cor=models.CharField(max_length=50)
    data_nascimento=models.DateField()
    descricao=models.TextField(blank=True,null=True) #esses dois parametros juntos deixam claro que o campo 'descricao' é opcional
    disponivel=models.BooleanField(default=True) #defalt = True significa que assim que o gato for cadastrado ele é marcado como disponivel
    raca=models.ForeignKey(Raca,on_delete=models.CASCADE,related_name='gatos') #atributo 'raca' é chave estrangeira da classe Raca; related_name injeta atributo 'gatos' na classe Raca, oque facilita pesquisa por filtragem