import conexao

#Criação da tabela Cliente
conexao.conectar()
def criar():
    criar_tabela = "CREATE TABLE IF NOT EXISTS cliente(nome string, sobrenome string, idade interger, cpf integer, telefone integer, endereco string, cidade string, estado string)"
    conexao.cursor.execute(criar_tabela)