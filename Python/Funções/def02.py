#EXEMPLO DE PROGRAMA COM FUNÇÃO PARA CALCULAR A MÉDIA

def calcular_media(nota1, nota2, nota3):

    media = (nota1 + nota2 + nota3) / 3
    return media

def condicoes():
    if resultado >= 7:
        print("APROVADO!!")

    else:

        print("REPROVADO!!")

#CORPO PRINCIPAL DO PROGRAMA 

#ENTRADA DE DADOS

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

#CHAMADA DA FUNÇÃO

resultado = calcular_media(n1,n2,n3)

#SAIDA DO RESULTADO

print(f"Sua média final e: {resultado: .2f}")

#CONDIÇÃO

condicoes()