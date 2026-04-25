#CRIA UM NOVO ARQUIVO OU SOBRESCREVE SE JÁ EXISTIR

with open("exemplo.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Olá, este é um arquivo criado em Python!\n")
    arquivo.write("Segunda linha.")

#LÊ O CONTEÚDO DE UM ARQUIVO EXISTENTE
    
with open("exemplo.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)