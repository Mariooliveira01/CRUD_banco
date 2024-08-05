def menu():
    print("---------------- MENU DE CLIENTES ----------------")
    print("O que deseja fazer:")
    print("1 - Cadastrar Clientes:\n2 - Exibir Clientes:\n3 - Consultar Cliente pelo CPF:\n4 - Alterar Dados Cadastrais:\n5 - Excluir Cliente:\n6 - Sair")
    print("--------------------------------------------------")
    global opcao
    opcao = input()
    return opcao