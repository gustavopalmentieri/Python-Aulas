import pandas as pd
import numpy as np #NUMERICAL PYTHON (BIBLIOTECA QUE MANIPULA MATRIZES)

#CRIAR UMA MATRIZ NUMPY (3 X 3)

matriz = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

#CONVERTER A MATRIZ EM DATAFRAME PANDAS

df = pd.DataFrame(matriz, columns=['A', 'B', 'C'], index=['Linha1', 'Linha2', 'Linha3'])

print(df)

#SAÍDA:

#         A B C
#LINHA1   1 2 3
#LINHA2   4 5 6
#LINHA3   7 8 9