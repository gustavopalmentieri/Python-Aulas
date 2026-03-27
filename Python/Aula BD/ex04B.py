#BANCO DE DADOS COM LAÇO DE REPETIÇÃO - PRIME KEY - DADOS AUTOMÁTICOS QUE O PROPRIO PYTHON COLOCA DE ACORDO COM O ATREIBUTO NA COLUNA E LINHA

import sqlite3
banco = sqlite3.connect('quarto_b_banco.db') #COLOCAR NO BANCO DO MANUAL
cursor = banco.cursor()

#cursor.execute("CREATE TABLE colaborador(id_cpf integer primary key AUTOINCREMENT NOT NULL, nome text, cargo text, idade integer, email text)") # Defini o id_cpf como Chave Primária (não permite números repetidos) e NOT NULL (obriga o preenchimento do campo), garantindo que cada contribuinte seja único e identificado.

cursor.execute("INSERT INTO colaborador (nome, cargo, idade, email) VALUES('Osvaldo', 'Gerente', 32, 'osvaldo@gmail.com')")
cursor.execute("INSERT INTO colaborador (nome, cargo, idade, email) VALUES('Yago', 'Jovem Aprendiz', 19, 'yago@gmail.com')")
cursor.execute("INSERT INTO colaborador (nome, cargo, idade, email) VALUES('Renata', 'Diretora', 50, 'renata@gmail.com')")

banco.commit()

cursor.execute("SELECT * FROM colaborador")

for colaborador in cursor.fetchall():
    print(colaborador)
