import sqlite3
from funcao_menu import menu
import conexao
import insert_cliente
import select_cliente
import criar_tabela
import update
import delete

#Criação da tabela Cliente
criar_tabela.criar()

opcao = menu()
while (opcao !='6'):

    if(opcao == '1'):
        insert_cliente.cadastrar_cliente()
    elif(opcao == '2'):
        select_cliente.exibir_cliente()
    elif(opcao == '3'):
        select_cliente.consultar_cliente()
    elif(opcao == '4'):
        update.alterar_dados()
    elif(opcao == '5'):
        delete.deletar()
    opcao = menu()