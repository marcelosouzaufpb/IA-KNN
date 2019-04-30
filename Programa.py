import Implementação

k = int(input(" Digite a Quantidade de Vizinhos(K): "))


listaDeTreinamento = Implementação.criaArquivoLista("treinamento.txt")

listaDeTeste = Implementação.criaArquivoLista("teste.txt")

listaDeResultadoTeste = Implementação.criaArquivoLista("rotulosteste.txt")


listaDeResultado = Implementação.CriaListaDeResultado(listaDeTreinamento, listaDeTeste, k)

Implementação.gravaListaDentroDoArquivo(listaDeResultado, "resultado.txt")


porcentagem = Implementação.CalculaPorcentagem(listaDeResultado, listaDeResultadoTeste)

print("O Classificador Obteve ", porcentagem,"% de acertos")
