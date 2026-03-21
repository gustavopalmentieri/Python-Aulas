#DELETANDO INFORMAÇÕES DO BANCO DE DADOS

import sqlite3
banco = sqlite3.connect('segundo_banco.db') #NESSA LINHA CRIA O BANCO DE DADOS
cursor = banco.cursor() #CURSOR E PARA PESQUISAR
#cursor.execute("CREATE TABLE pessoas(nome text, idade integer, email text)") #NESSA LINHA CRIA A TABELA
#PARA ACESSAR OS DADOS NO BANCO DE DADOS DB

cursor.execute("DELETE FROM pessoas")
banco.commit() #SEMPRE COLOCAR O COMMIT EM BAIXO DA FUNÇÃO PARA DELETAR

print(cursor.fetchall())