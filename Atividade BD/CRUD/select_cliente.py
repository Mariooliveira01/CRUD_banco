import sqlite3
import conexao

def exibir_cliente():
    conexao.conectar()
    resultado = conexao.cursor.execute("SELECT * FROM cliente").fetchall()
    for result in resultado:
        print("--------------------------------------------------")
        print("Nome: ",result[0])
        print("Sobrenome: ",result[1])
        print("Idade: ",result[2])
        print("CPF:",result[3])
        print("Telefone: ",result[4])
        print("Endereço: ",result[5])
        print("Cidade: ",result[6])
        print("Estado: ",result[7])
        print("--------------------------------------------------")
    #conexao.conn.close()
        
def consultar_cliente():
    conexao.conectar()
    cpf = input("Qual o CPF Deseja Consultar: ")
    try:
        resultado = conexao.conn.execute('''SELECT * FROM cliente WHERE cpf = ?''',(cpf,)).fetchall()
        if(resultado == []):
            print("CPF não encontrado")
        else:
            for result in resultado:
                print("--------------------------------------------------")
                print("Nome: ",result[0])
                print("Sobrenome: ",result[1])
                print("Idade: ",result[2])
                print("CPF:",result[3])
                print("Telefone: ",result[4])
                print("Endereço: ",result[5])
                print("Cidade: ",result[6])
                print("Estado: ",result[7])
        return cpf
    except sqlite3.Error as erro:
        print("Erro ao tentar encontrar o CPF. ",erro)
    #conn.close