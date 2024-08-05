import sqlite3
import conexao

#Criação uma função para coletar dados do cliente
def cadastrar_cliente():
    try:
        conexao.conectar()
        nome = input("Informe o seu Nome: ")
        sobrenome = input("Informe o seu Sobrenome: ")
        idade = int(input("Informe a sua Idade: "))
        cpf = int(input("Informe o seu CPF: "))
        telefone = input("Informe o seu Nº de Telefone: ")
        endereco = input("Informe o seu Endereço: ")
        cidade = input("Informe a sua Cidade: ")
        estado = input("Informe o seu Estado: ")

        inserir_cliente = "INSERT INTO cliente VALUES ('"+nome+"','"+sobrenome+"','"+str(idade)+"','"+str(cpf)+"','"+str(telefone)+"','"+endereco+"','"+cidade+"','"+estado+"')"
        conexao.cursor.execute(inserir_cliente)
        conexao.conn.commit()
        conexao.conn.close()
        print("Cliente cadastrado com sucesso!")
    except sqlite3.Error as erro:
        print("Erro ao cadastrar Cliente", erro)