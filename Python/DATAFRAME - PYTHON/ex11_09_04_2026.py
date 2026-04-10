#DATAFRAME EM PYTHON

import pandas as pd

#CRIANDO UM DATAFRAME A PARTIR DE UM DICIONÁRIO

data = {

    'Nome': ['Inacio', 'José', 'Eduardo'],
    'Idade': [56, 77, 91],
    'Estado': ['BA', 'RS', 'PE']
}
 
df = pd.DataFrame(data)

#SELECIONAR MÚLTIPLAS COLUNAS:

print(df[['Nome','Idade']])

