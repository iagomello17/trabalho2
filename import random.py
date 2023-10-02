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

def calcular_media(notas):
    notas = [float(nota) for nota in notas.split()]
    return sum(notas) / len(notas)

def criar_arquivos():
    alunos = ["João", "Maria", "Pedro"]
    notas = ["8.5 7.0 9.5", "6.0 7.5 8.0", "9.0 8.5 9.5"]

    with open("alunos.txt", "w") as arquivo_alunos, open("notas.txt", "w") as arquivo_notas:
        for aluno, nota in zip(alunos, notas):
            arquivo_alunos.write(f"{aluno}\n")
            arquivo_notas.write(f"{nota}\n")

def gerar_arquivo_medias(nome_alunos, nome_notas, nome_resultado):
    linhas_alunos = open(nome_alunos, "r").readlines()
    linhas_notas = open(nome_notas, "r").readlines()

    with open(nome_resultado, "w") as arquivo_resultado:
        for linha_aluno, linha_notas in zip(linhas_alunos, linhas_notas):
            nome_aluno = linha_aluno.strip()
            media = calcular_media(linha_notas)
            arquivo_resultado.write(f"{nome_aluno}: {media}\n")

criar_arquivos()

gerar_arquivo_medias("alunos.txt", "notas.txt", "medias.txt")
'''

#EXERCICO 5
def alterar_nota(nome_aluno, nota_antiga, nova_nota):
    # Ler os dados dos arquivos
    with open("alunos.txt", "r") as arquivo_alunos, open("notas.txt", "r") as arquivo_notas:
        linhas_alunos = arquivo_alunos.readlines()
        linhas_notas = arquivo_notas.readlines()

    try:
        indice_aluno = linhas_alunos.index(nome_aluno + '\n')
    except ValueError:
        print(f"O aluno '{nome_aluno}' não foi encontrado.")
        return

   
    linhas_notas[indice_aluno] = nova_nota + '\n'

    
    with open("alunos.txt", "w") as arquivo_alunos, open("notas.txt", "w") as arquivo_notas:
        arquivo_alunos.writelines(linhas_alunos)
        arquivo_notas.writelines(linhas_notas)

alterar_nota("João", "8.5 7.0 9.5", "8.0 7.0 9.5")



#EXERCICO 6

def separar_enderecos_ip(arquivo_entrada, arquivo_validos, arquivo_invalidos):
    with open(arquivo_entrada, "r") as entrada, open(arquivo_validos, "w") as validos, open(arquivo_invalidos, "w") as invalidos:
        for linha in entrada:
            endereco = linha.strip().split(".")
            if len(endereco) == 4:
                octetos_validos = True
                for octeto in endereco:
                    if not (octeto.isdigit() and 0 <= int(octeto) <= 255):
                        octetos_validos = False
                        break
                if octetos_validos:
                    validos.write(linha)
                else:
                    invalidos.write(linha)
            else:
                invalidos.write(linha)

# Exemplo de uso
separar_enderecos_ip("enderecos.txt", "validos.txt", "invalidos.txt")

'''
