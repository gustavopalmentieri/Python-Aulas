#BANCO DE DADOS EM PYTHON - INSERINDO MAIS DE UMA INFORMAÇÃO NO BANCO

import sqlite3
banco = sqlite3.connect('segundo_banco.db') #NESSA LINHA CRIA O BANCO DE DADOS
cursor = banco.cursor() #CURSOR E PARA PESQUISAR
#cursor.execute("CREATE TABLE pessoas(nome text, idade integer, email text)") #NESSA LINHA CRIA A TABELA
#cursor.execute("INSERT INTO pessoas VALUES('Kaiki', 16, 'kaiki.official@gmail.com')")
#cursor.execute("INSERT INTO pessoas VALUES('Gustavo', 18, 'lrgtvmito@gmail.com')")
#cursor.execute("INSERT INTO pessoas VALUES('Kaiki', 16, 'kaiki.official@gmail.com')")
#cursor.execute("INSERT INTO pessoas VALUES('Gustavo', 18, 'lrgtvmito@gmail.com')")
banco.commit()

#PARA ACESSAR OS DADOS NO BANCO DE DADOS DB

cursor.execute("SELECT * FROM pessoas")
print(cursor.fetchall())
