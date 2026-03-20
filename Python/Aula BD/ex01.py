#BANCO DE DADOS EM PYTHON - INSERINDO MAIS DE UMA INFORMAÇÃO NO BANCO

import sqlite3
banco = sqlite3.connect('segundo_banco.db')
cursor = banco.cursor()
cursor.execute("CREATE TABLE pessoas(nome text, idade integer, email text)")
cursor.execute("INSERT INTO pessoas VALUES('Gustavo', 18, 'lrgtvmito@gmail.com')")
cursor.execute("INSERT INTO pessoas VALUES('Kaiki', 16, 'kaiki.official@gmail.com')")
banco.commit()

#PARA ACESSAR OS DADOS NO BANCO DE DADOS DB

cursor.execute("SELECT * FROM pessoas")
print(cursor.fetchall())
