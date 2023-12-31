pecas_disponiveis = [("Troca de oleo", 250.0), ("Bateria 60PD", 334.0), ("PNEU 165/60 r13", 434.0),("Correia", 50.0)]


lista_vendas = []

def exibir_catalogo():
    print("Catálogo de Peças Disponíveis:")
    for i, (peca, preco) in enumerate(pecas_disponiveis, start=1):
        print(f"{i}. {peca} - R${preco:.2f}")

def realizar_venda():
    exibir_catalogo()
    escolha = int(input("Digite o número da peça que deseja comprar (ou 0 para sair): "))
    
    if escolha == 0:
        return
    elif escolha < 1 or escolha > len(pecas_disponiveis):
        print("Escolha inválida. Tente novamente.")
    else:
        quantidade = int(input(f"Quantidade de '{pecas_disponiveis[escolha - 1][0]}': "))
        if quantidade > 0:
            lista_vendas.append((pecas_disponiveis[escolha - 1][0], quantidade, pecas_disponiveis[escolha - 1][1]))
            print(f"{quantidade} '{pecas_disponiveis[escolha - 1][0]}'(s) adicionado(s) ao carrinho./n")
            realizar_venda() 
        else:
            print("Quantidade inválida. Tente novamente.")

def remover_item():
    if not lista_vendas:
        print("Nenhum item no carrinho para remover.")
        return

    print("/nItens no Carrinho:")
    for i, (peca, quantidade, preco) in enumerate(lista_vendas, start=1):
        print(f"{i}. {peca} - Quantidade: {quantidade} - Preço unitário: R${preco:.2f}")

    escolha = int(input("Digite o número do item que deseja remover (ou 0 para sair): "))
    
    if escolha == 0:
        return
    elif escolha < 1 or escolha > len(lista_vendas):
        print("Escolha inválida. Tente novamente.")
    else:
        item_removido = lista_vendas.pop(escolha - 1)
        print(f"'{item_removido[0]}' removido do carrinho.")


def calcular_total():
    total = sum(preco * quantidade for _, quantidade, preco in lista_vendas)
    return total

def concluir_venda():
    if not lista_vendas:
        print("Nenhum item no carrinho.")
        return
    
    print("\nItens no Carrinho:")
    for peca, quantidade, preco in lista_vendas:
        print(f"{peca} - Quantidade: {quantidade} - Preço unitário: R${preco:.2f}")
    
    total = calcular_total()
    print(f"Total da compra: R${total:.2f}")
    
    pagamento = float(input("Digite o valor pago pelo cliente: "))
    
    if pagamento < total:
        print("Valor insuficiente. Tente novamente.")
    else:
        troco = pagamento - total
        print(f"Troco: R${troco:.2f}")
        print("Venda concluída com sucesso!")
        lista_vendas.clear()

def main():
    while True:
        print("\nMenu:")
        print("1. Realizar Venda")
        print("2. Concluir Venda")
        print("3. Remover Item do Carrinho")
        print("4. Sair")
        
        escolha = int(input("Escolha uma opção: "))
        
        if escolha == 1:
            realizar_venda()
        elif escolha == 2:
            concluir_venda()
        elif escolha == 3:
            remover_item()
        elif escolha == 4:
              print("Saindo do programa.")
              break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
