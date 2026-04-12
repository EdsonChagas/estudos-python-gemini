# Exercício - Mini sistema de pedidos para uma frutaria

# Lista vazia para adicionar os itens
carrinho = []

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
total_conta = 0

# Estrutura de repetição para a compra das frutas
while len(carrinho) < 3:
    fruta = input(f"Item {len(carrinho) + 1}/3 - Qual fruta gostaria de comprar: ").lower()
    
    # Condição para verificar se tem ou não a fruta escolhida na lista
    if fruta in precos:
        carrinho.append(fruta)
        # Pega o valor dos itens e faz a soma dos mesmos
        total_conta += precos[fruta]
        # Imprime o nome da fruta e seu valor unitário
        print(f"{fruta.capitalize()} adicionado: R$ {precos[fruta]:.2f}")
    else:
        print("Sinto muito, não temos essa fruta em estoque.")
    
print("---RESUMO DA COMPRA---")
print(f"Itens no carrinho: {carrinho}")
print(f"Valor total da compra R$ {total_conta:.2f}")
