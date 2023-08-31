

#EXERCICIO 1
''''
def soma(n):
    if n <= 0:
        return 0
    else:
        return n + soma(n - 1)

numero = int(input("Digite um número inteiro positivo: "))
resultado = soma(numero)
print(f"A soma dos primeiros {numero} números inteiros positivos é: {resultado}")

#EXERCICIO 2

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)


numero1 = int(input("Digite um número inteiro positivo: "))
resultado1 = fatorial(numero1)
print(f"O fatorial de {numero1} é: {resultado1}")


#EXERCICIO 3 

def inverter(txt):
    return txt[::-1]

palavra = input("digite uma palavra:")

print(inverter(f"{palavra}"))


#EXERCICO 4

def decimal_para_binario(decimal):
    pilha = []
    
    if decimal == 0:
        return "0"
    
    while decimal > 0:
        pilha.append(decimal % 2)
        decimal //= 2
    
    binario = ""
    while len(pilha) > 0:
        binario += str(pilha.pop())
    
    return binario


numero = int(input("escreva um numero positivo:"))
binario_resultante = decimal_para_binario(numero)
print(f"O número {numero} em binário é: {binario_resultante}")
'''

#EXERCICIO 5 

class EditorDeTexto:
    def __init__(self):
        self.texto = ""
        self.comandos = []
    
    def inserir_texto(self, novo_texto):
        self.comandos.append(self.texto)
        self.texto += novo_texto
    
    def desfazer(self):
        if self.comandos:
            self.texto = self.comandos.pop()
    
    def mostrar_texto(self):
        print("Texto atual:", self.texto)

editor = EditorDeTexto()

editor.inserir_texto(input("insira um texto:"))
editor.mostrar_texto()

editor.desfazer()
editor.mostrar_texto()
