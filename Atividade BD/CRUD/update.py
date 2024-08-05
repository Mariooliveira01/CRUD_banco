import conexao
import select_cliente

def alterar_dados():
    conexao.conectar()
    print("------------- Alteraração de Dados ---------------")
    global cpfPesquisar
    cpfPesquisar = select_cliente.consultar_cliente()

    if(cpfPesquisar != []):
        dado_update = input("qual sera alterado?\nnome\nsobrenome\nidade\ncpf\ntelefone\nendereço\ncidade\nestado\n ").lower()
        atualizacao(dado_update)

def atualizacao(dado_update):
    conexao.conectar()
    if dado_update == 'nome':
        novo_nome = input("Qual o novo Nome: ")
        conexao.cursor.execute("UPDATE cliente SET nome = '"+novo_nome+"' WHERE cpf = ?",(cpfPesquisar,))
        print("Nome alterado com sucesso. ")

    elif dado_update == 'sobrenome':
        novo_sobrenome = input("Qual o novo Sobrenome: ")
        conexao.cursor.execute("UPDATE cliente SET sobrenome = '"+novo_sobrenome+"' WHERE cpf = ?",(cpfPesquisar,))
        print("Sobrenome alterado com sucesso. ")

    elif dado_update == 'idade':
        nova_idade = input("Qual o novo Idade: ")
        conexao.cursor.execute("UPDATE cliente SET idade = '"+nova_idade+"' WHERE cpf = ?",(cpfPesquisar,))
        print("Idade alterada com sucesso. ")

    elif dado_update == 'cpf':
        novo_cpf = input("Qual o novo CPF: ")
        conexao.cursor.execute("UPDATE cliente SET cpf = '"+novo_cpf+"' WHERE cpf = ?",(cpfPesquisar,))
        print("CPF alterado com sucesso. ")

    elif dado_update == 'telefone':
        novo_telefone = input("Qual o novo Telefone: ")
        conexao.cursor.execute("UPDATE cliente SET telefone = '"+novo_telefone+"' WHERE cpf = ?",(cpfPesquisar,))
        print("Telefone alterado com sucesso. ")

    elif dado_update == 'endereco':
        novo_endereco = input("Qual o novo endereco: ")
        conexao.cursor.execute("UPDATE cliente SET endereco = '"+novo_endereco+"' WHERE cpf = ?",(cpfPesquisar,))
        print("Endereço alterado com sucesso. ")

    elif dado_update == 'sobrenome':
        novo_sobrenome = input("Qual o novo nome: ")
        conexao.cursor.execute("UPDATE cliente SET nome = '"+novo_sobrenome+"' WHERE cpf = ?",(cpfPesquisar,))
        print("Sobrenome alterado com sucesso. ")

    else:
        print("Deu ruim, tente novamente.")
    conexao.conn.commit()