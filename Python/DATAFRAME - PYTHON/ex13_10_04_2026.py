import numpy as np

#LISTA DE LISTAS (3 X 2)

lista = [
    [1, 2],
    [3, 4],
    [5, 6]
]

matriz = np.array(lista)

print(matriz)

#SAÍDA:
# [[1 2]
#  [3 4]
#  [5 6]]

#TRANSFORMAR EM LISTA ÚNICA E EM MATRIZ (2 X 3)

lista_unica = [[1, 2, 3, 4, 5, 6]]

matriz_2x3 = np.array(lista_unica).reshape(2, 3) #RESHAPE É A FORMA QUE AQUILO VAI SER (NO CASO UMA MATRIZ COM 2 COLUNAS E 3 LINHAS)
print(matriz_2x3)
