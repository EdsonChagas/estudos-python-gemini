# Exercício - Mini sistema de pedidos para uma frutaria

# Função para verificar se tem ou não a fruta escolhida
def verificar_estoque(fruta, precos):
    if fruta in precos:
        return precos[fruta]
    else:
        return None
    
# Função para o calcúlo do troco
def calcular_troco(total_compra, valor_pago):
    return valor_pago - total_compra

# Função para exibir tabela de preço das frutas
def exibir_menu(tabela_precos):
    print("------- MENU DE HOJE -------")
    for fruta, preco in tabela_precos.item():
        print(f"{fruta.capitalize()}: R$ {precos:.2f}")
    print("--------------------")

# Biblioteca de itens de frutas com seus respectivos valores
precos = {
    "abacaxi": 5.00,
    "acerola": 1.20,
    "banana": 2.60,
    "cajá": 1.10,
    "caju": 2.00,
    "goiaba": 5.50,
    "laranja": 4.00,
    "limão": 6.00,
    "maçã": 2.30,
    "manga": 9.00,
    "mangaba": 1.50,
    "maracujá": 8.00,
    "pêra": 2.00,
    "umbu": 1.20,
    "uva": 5.50,   
}
# Total da conta a pagar iniciado em 0
total_compra = 0
# Lista vazia para adicionar os itens
carrinho = []

exibir_menu(tabela_precos)

# Estrutura de repetição para a compra das frutas
while len(carrinho) < 3:
    fruta = input(f"Item {len(carrinho) + 1}/3 - Qual fruta gostaria de comprar: ").lower();
    
    # Chama a função e guarda numa variável
    preco_encontrado = verificar_estoque(fruta, precos)
    
    # Condição para verificar se tem ou não a fruta escolhida na lista
    if preco_encontrado is not None:
        carrinho.append(fruta)
        total_compra += precos[fruta]
        # Imprime o nome da fruta e seu valor unitário
        print(f"{fruta.capitalize()} adicionado: R$ {preco_encontrado:.2f}")
    else:
        print("Sinto muito, não temos essa fruta em estoque.")
        
    
print("---RESUMO DA COMPRA---")
print(f"Itens no carrinho: {carrinho}")
print(f"Valor total da compra R$ {total_compra:.2f}")

pagamento = float(input("\nQuanto você vai dar em dinheiro? R$ "))
# Chama a função e guarda na variável
meu_troco = calcular_troco(total_compra, pagamento)

# Condição para informar se falta dinheiro para concluir a compra e informar o troco
if meu_troco < 0:
    print(f"Ops! Ainda faltam R$ {abs(meu_troco):.2f}")
else:
    print(f"Seu troco é R$ {meu_troco:.2f}")
