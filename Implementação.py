from math import *
import copy


def criaArquivoLista(NomeDoArquivo): #Criar Arquivos e colocar dentro de uma lista
    arquivo = open(NomeDoArquivo,"r")
    lista = arquivo.readlines()
    arquivo.close()
    return lista


def gravaListaDentroDoArquivo(lista, NomeDoArquivo): 
    arquivo = open(NomeDoArquivo,"w")
    for i in lista:
        arquivo.write(i+"\n")
    arquivo.close()


def CalculaDistancia(flor1, flor2): #Distancia Euclidiana
    return sqrt( ((float(flor1[0])-float(flor2[0]))**2) + ((float(flor1[1])-float(flor2[1]))**2) + ((float(flor1[2])-float(flor2[2]))**2) + ((float(flor1[3])-float(flor2[3]))**2) )

	
	
def ObterRotuloEscolhido(rotulos):
    if(len(rotulos) == 1):
        return rotulos[0]
    else:
        escolhido = rotulos[0]
        for i in range(1,len(rotulos)): # Count retorna a quantidade de ocorrências 
            if(rotulos.count(rotulos[i]) > rotulos.count(escolhido)): #Procura descobrir o menor varrendo os rótulos e retorna o que mais tiver ocorrência
                escolhido = rotulos[i]
        return escolhido

def ObterKMaisProximos(flor, ListaDeTreinamento, k):
    NovaListaDeTreinamento = copy.copy(ListaDeTreinamento) #Clone para que o original não sofra mudanças e altere o programa. 
    lista_dos_mais_proximos = [] 
    for i in range(k): 
        mais_proximo = NovaListaDeTreinamento[0].split(",")
        indice = 0
        for i in range(1,len(NovaListaDeTreinamento)):
            if(CalculaDistancia(flor, NovaListaDeTreinamento[i].split(",")) < CalculaDistancia(flor, mais_proximo)):
                mais_proximo = NovaListaDeTreinamento[i].split(",")
                indice = i
        lista_dos_mais_proximos.append(mais_proximo[4][:-1])#adiciona no ultimo elemento
        del NovaListaDeTreinamento[indice]
    return lista_dos_mais_proximos
    
def CriaListaDeResultado(ListaDeTreinamento, lista_de_teste, k):
    resultado = []
    for i in lista_de_teste:
        flor = i.split(",")  
        RotuloDaFlor = ObterKMaisProximos(flor, ListaDeTreinamento, k)
        rotulo = ObterRotuloEscolhido(RotuloDaFlor)
        resultado.append(rotulo)
    return resultado

def CalculaPorcentagem(resultado, ResultadoDoTeste):
    acertos = 0
    for i in range(len(resultado)):
        if(resultado[i]+"\n" == ResultadoDoTeste[i]):
            acertos+=1
    porcentagem = (100*acertos)//len(resultado)
    return porcentagem


