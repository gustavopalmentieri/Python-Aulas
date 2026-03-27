#BANCO DE DADOS COM LAÇO DE REPETIÇÃO

import sqlite3
banco = sqlite3.connect('terceiro_banco.db') #NESSA LINHA CRIA O BANCO DE DADOS
cursor = banco.cursor() #CURSOR E PARA PESQUISAR
cursor.execute("CREATE TABLE IF NOT EXISTS alunos(nome text, idade integer, email text)") #NESSA LINHA CRIA A TABELA
cursor.execute("INSERT INTO alunos VALUES('Kaiki', 16, 'kaikiofficial@gmail.com')")
cursor.execute("INSERT INTO alunos VALUES('Gustavo', 18, 'gustavo@gmail.com')")
cursor.execute("INSERT INTO alunos VALUES('Hector', 28, 'hector@gmail.com')")
cursor.execute("ALTER TABLE alunos ADD COLUMN cpf integer") #ALTERANDO A TABELA E INSERINDO UM ATRIBUTOS - POSSO TER QUANTOS "ALTER TABLE" QUE EU PRECISAR;
banco.commit()

#PARA ACESSAR OS DADOS NO BANCO DE DADOS DB COM A CLASULA LAÇOS DE REPETIÇÃO FOR

cursor.execute("SELECT * FROM alunos")

for aluno in cursor.fetchall(): #NESSE CASO O FOR QUEBRA A LINHA ENTRE AS INFORMAÇÕES IMPRIMIDAS NO BANCO DE DADOS
    print(aluno)