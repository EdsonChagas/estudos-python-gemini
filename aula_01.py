# Exercício - O Assistente de Banho

# Estrutura de repetição para perguntar a temperatura mais de uma vez
while True:
    temperatura_agua = float(input("Qual a temperatura da água agora: "))
    # Condição para saber a temperatura da água
    if temperatura_agua < 30:
        print("Muito frio! ❄️")
    elif 30 <= temperatura_agua <= 40:
        print("Está perfeito! 🛁")
    else:
        print("Cuidado, muito quente! 🔥")
    
    # Condição para solicitar uma nova temperatura
    sair = input("Gostaria de escolher uma nova temperatura (s/n): ")
    if sair == "n":
        break
