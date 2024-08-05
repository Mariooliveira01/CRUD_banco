import sqlite3

def deletar():
    cpf = input("Qual CPF deseja deletar: ")
    try:
        banco = sqlite3.connect('cadastro.db') 
        cursor = banco.cursor()
        cursor.execute("DELETE from cliente WHERE cpf = ?",(cpf,))
        banco.commit()
        banco.close()
        print("Os seus dados foram removidos com sucesso!")
    except sqlite3.Error as erro:
        print("Erro ao Excluir: ",erro)