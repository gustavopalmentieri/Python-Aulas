#BANCO DE DADOS COM LAÇO DE REPETIÇÃO - PRIME KEY - UPDATE

import sqlite3
banco = sqlite3.connect('quarto_b_banco.db') #UM BANCO DE DADOS JÁ CRIADO - O UPDATE VAI ATUALIZAR ATRAVÉS DAS INFORMAÇÕES PRESENTES NESSE BANCO
cursor = banco.cursor()

#cursor.execute("CREATE TABLE devedor(id_cpf integer primary key AUTOINCREMENT NOT NULL, nome text, idade integer, email text)")

cursor.execute("UPDATE colaborador SET nome = 'Vasconcelos' WHERE id_cpf = 334;") #AQUI ESTOU ALTERANDO ATRAVÉS DA PRIME KEY SÓ E POSSIVEL ALTERAR ATRAVÉS DELA - PODENDO ALTERAR QAULQUER ATRIBUTO, NO CASO ALTEREI O NOME DA PESSOA QUE TINHA O CPF NO BANCO DE DADOS REGISTRADO COMO '334'

#EXEMPLO DE ALTERAÇÃO DE MAIS ATRIBUTOS:

#cursor.execute("UPDATE colaborador SET nome = 'Vasconcelos', SET idade = 20, SET email = 'vasconcelos@gmail.com' WHERE id_cpf = 334;")

banco.commit()

cursor.execute("SELECT * FROM colaborador")

for colaborador in cursor.fetchall():
    print(colaborador)
