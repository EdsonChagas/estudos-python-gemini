# Exercício - Mini sistema de pedidos para uma frutaria

frutas_disponiveis = ["abacaxi", "abiu", "acerola", "açaí", "amora", "araçá", "banana", "biribá", "cacau", "cajá", "caju", "cambuí", "cereja", "ciriguela", "cupuaçu", "goiaba", "guaraná", "jabuticaba", "jatobá", "jenipapo", "jurubeba", "laranja", "limão", "macaúba", "maçã","mandacaru", "manga","mangaba", "maracujá", "pequi", "pêra", "pitanga", "tucumã", "umbu", "uva"]

carrinho = []

while len(carrinho) < 3:
    fruta = input(f"Item {len(carrinho) + 1}/3 - Qual fruta gostaria de comprar: ").lower()
    
    # Condição para verificar se tem ou não a fruta escolhida na lista
    if fruta in frutas_disponiveis:
        carrinho.append(fruta)
        print(f"{fruta.capitalize()} adicionado.")
    else:
        print("Sinto muito, não temos essa fruta em estoque.")
        

print("---RESUMO DA COMPRA---")
print(f"Itens no carrinho: {carrinho}")
