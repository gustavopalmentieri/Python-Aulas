#BANCO DE DADOS EM PYTHON
#EXTENSÃO SQL DB VIEWER - PARA VISUALIZAR O BANCO DE DADOS

import sqlite3 #IMPORTANDO UM BANCO DE DADOS DA BIBLIOTECA DO PYTHON
banco = sqlite3.connect('treinando_banco.db') #NOMEANDO O NOME DO BANCO DE DADOS E INSERINDO EM UMA VARIÁVEL
cursor = banco.cursor()
cursor.execute("CREATE TABLE pessoas(nome text, idade integer, email text)")
cursor.execute("INSERT INTO pessoas VALUES('Gustavo', 63, 'lrgtvmito@gmail.com')") #COLOCANDO AS INFORMAÇÕES NO BANCO DE DADOS - TABELA
banco.commit() #INSERINDO (CONFIRMANDO) AS INFORMAÇÕES PARA SEREM UPADAS NO BANCO DE DADOS

#PARA ACESSAR OS DADOS NO BANCO DE DADOS DB

cursor.execute("SELECT * FROM pessoas")
print(cursor.fetchall())
