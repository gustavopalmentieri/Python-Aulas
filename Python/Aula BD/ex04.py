#BANCO DE DADOS COM LAÇO DE REPETIÇÃO - PRIME KEY - DADOS MANUAL

import sqlite3
banco = sqlite3.connect('quarto_banco.db')
cursor = banco.cursor()

cursor.execute("CREATE TABLE contribuinte(id_cpf integer primary key NOT NULL, nome text, idade integer, email text)") # Defini o id_cpf como Chave Primária (não permite números repetidos) e NOT NULL (obriga o preenchimento do campo), garantindo que cada contribuinte seja único e identificado.

cursor.execute("INSERT INTO contribuinte VALUES(013, 'Arnaldo', 32, 'arnaldo@gmail.com')")
cursor.execute("INSERT INTO contribuinte VALUES(014, 'Lizandra', 21, 'lizandra@gmail.com')")
cursor.execute("INSERT INTO contribuinte VALUES(015, 'Tiago', 29, 'tiago@gmail.com')")
banco.commit()

cursor.execute("SELECT * FROM contribuinte")

for contribuinte in cursor.fetchall():
    print(contribuinte)
