# Execercício - O Validador de Senhas

lista_item = []
# Estrutura de repetição para cadastro de senha
while True:
    senha = input("Digite sua senha: ")
    # Conta quantos caracteres tem a senha digitada
    tamanho_senha = len(senha)
    # Condição para confirmar o tamanhdo da senha e seguir com o cadastro
    if tamanho_senha >= 8:
        print("Senha cadastrada com sucesso!")
        break
    else:
        print("Senha muito curta!")
    
# Estrutura de repetição para a compra de 3 itens
while len(lista_item) < 3:
    item = input("Escolha um item: ")
    # Adiciona os itens digitados na lista
    lista_item.append(item)
    print(f"Você já tem {len(lista_item)} itens.")

print("Maravilha, sua compra foi concluída!")
