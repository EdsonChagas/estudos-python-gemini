# Execercício - O Validador de Senhas

# Estrutura de repetição para cadastro de senha
while True:
    senha = input("Digite sua senha: ")
    tamanho_senha = len(senha)
    # Condição para confirmar o tamanhdo da senha e seguir com o cadastro
    if tamanho_senha >= 8:
        print("Senha cadastrada com sucesso!")
        break
    else:
        print("Senha muito curta!")
