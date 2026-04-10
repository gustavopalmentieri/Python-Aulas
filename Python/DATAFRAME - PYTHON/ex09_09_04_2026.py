#DATAFRAME EM PYTHON

import pandas as pd

#CRIANDO UM DATAFRAME A PARTIR DE UM DICIONÁRIO

data = {

    'Nome': ['Ana', 'Bruno', 'Carlos'],
    'Idade': [25, 30, 22],
    'Estado': ['SP', 'RJ', 'BH']
}

df = pd.DataFrame(data)

#EXIBINDO DATAFRAME:

print(df)

#ACESSANDO UMA COLUNA:

print(df['Nome'])

#FILTRANDO DADOS -> IDADE MAIOR QUE 23:

print(df[df['Idade'] > 23])