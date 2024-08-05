import sqlite3

nome = input("Informe seu nome: ")
idade = input("Informe sua idade: ")
email = input("Informe seu Email: ")

banco = sqlite3.connect('primeiro_banco.db') #criação do banco

cursor = banco.cursor()

#cursor.execute("CREATE TABLE pessoas (nome text,idade integer, email text)")

#cursor.execute("INSERT INTO pessoas VALUES('"+nome+"',"+str(idade)+",'"+email+"')")

cursor.execute("UPDATE pessoas SET nome = 'Osvaldino' WHERE idade = 25")

banco.commit()
cursor.execute("SELECT * FROM pessoas")
print(cursor.fetchall())