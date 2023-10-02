import random
'''
def escreverNumerosAleatorios(qtdNumeros, nomeArquivo):
    arquivoNumero = open(nomeArquivo, 'w')
    for i in range(qtdNumeros):
        arquivoNumero.write(str(random.randint(0,100)))
        arquivoNumero.write("\n")
    arquivoNumero.close()
escreverNumerosAleatorios(100,'aleatorios.txt')

def escreverMedia(qtdNumeros,nomeArquivo):
    arquivoNumeros = open(nomeArquivo)
    soma = 0
    for i in range(qtdNumeros):
        num = float(arquivoNumeros.readline())
        soma += num
    arquivoNumeros.close()
    return soma/qtdNumeros
print(escreverMedia(100, 'aleatorios.txt'))

def copArquivo(velhoArquivo, novoArquivo):
    f1 = open(velhoArquivo, 'r')
    f2 = open(novoArquivo, 'w')
    for texto in f1:
        f2.write(texto)
    f1.close()
    f2.close()
copArquivo("aleatorios.txt", "novo,txt")

#EXERCICIO 1 E 2 

import random

nomes = ["Alice", "Bob", "Carlos", "David", "Eva", "Fernanda", "Gabriel", "Heloisa", "Isabel", "Joao"]
sobrenomes = ["Silva", "Santos", "Pereira", "Oliveira", "Ferreira", "Rodrigues", "Almeida", "Carvalho", "Gomes", "Martins"]

def gerar_idade():
    return random.randint(1, 100)

def altura_pessoa():
    n = round(random.uniform(1.50, 2),2)
    return n

N = int(input("Digite o número de nomes a serem gerados: "))

with open("nomes_idades.txt", "w") as arquivo:
    for _ in range(N):
        nome = nomes[random.randint(0, len(nomes) - 1)]
        sobrenome = sobrenomes[random.randint(0, len(sobrenomes) - 1)]
        idade = gerar_idade()
        nome_completo = f"{nome} {sobrenome}"
        altura = altura_pessoa()
        arquivo.write(f"{nome_completo}: {idade} anos, altura: {altura}\n",)

print(f"{N} nomes e idades gerados") 

#EXERCICIO 3

def nomes(NOME):
    arquivonomes = open(NOME, 'w')
    N = input("Digite um nome: ")
    i = input("Digite um nome: ")
    arquivonomes.write(N + '\n')
    arquivonomes.write(i + '\n')
    arquivonomes.close()

nomes("arquivonomes.txt")

def copArquivo(velhoArquivo, novoArquivo):
    f1 = open(velhoArquivo, 'r')
    f2 = open(novoArquivo, 'w')
    for texto in f1:
        f2.write(texto)
    f1.close()
    f2.close()
copArquivo("arquivonomes.txt", "novo,txt")
'''
#EXERCICIO 4
