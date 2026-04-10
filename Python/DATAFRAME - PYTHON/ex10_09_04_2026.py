#DATAFRAME EM PYTHON

import pandas as pd

#CRIANDO UM DATAFRAME A PARTIR DE UM DICIONÁRIO

data = {

    'Nome': ['Ana', 'Bruno', 'Carlos'],
    'Idade': [25, 30, 22],
    'Estado': ['SP', 'RJ', 'BH']
}

df = pd.DataFrame(data)

#VISUALIZAR AS PRIMEIRAS LINHAS:

print(df.head())

