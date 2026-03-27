#BANCO DE DADOS EM PYTHON - MOSTRAR APENAS O USUÁRIO QUE TEM A IDADE IGUAL A 18!

import sqlite3 
banco = sqlite3.connect('terceiro_banco.db')
cursor = banco.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS funcionarios(nome text, idade integer, email text)") #"IF NOT EXISTS" - CRIE A TABELA SE NÃO EXISTIR A TABELA É A MESMO COISA DE COMENTAR IGUAL AOS OUTROS ARQUIVOS - SÓ FUNCIONA NO CREATE
cursor.execute("INSERT INTO funcionarios VALUES('Gustavo', 18, 'lrgtvmito@gmail.com')")
cursor.execute("INSERT INTO funcionarios VALUES('Kaiki', 16, 'kaiki.official@gmail.com')")
banco.commit()

#PARA ACESSAR OS DADOS NO BANCO DE DADOS DB COM A CLAUSULA WHERE

idade_sel = 18
cursor.execute("SELECT * FROM funcionarios where idade =?", (idade_sel,))
print(cursor.fetchall())
