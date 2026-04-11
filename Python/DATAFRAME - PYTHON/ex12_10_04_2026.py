#DATAFRAME EM PYTHON

import pandas as pd

#CRIANDO UM DATAFRAME A PARTIR DE UM DICIONÁRIO

data = {

    'Nome': ['Inacio', 'José', 'Eduardo'],
    'Idade': [56, 77, 91],
    'Estado': ['BA', 'RS', 'PE']
}
 
df = pd.DataFrame(data)

#FILTRAR COM DUAS CONDIÇÕES (USE "&" PARA E, "|" PARA OU)
#EXEMPLO: IDADE MAIOR QUE 20 E CIADADE IGUAL A ALGUM ESTADO DA TABELA

filtro = df[(df['Idade'] > 20) & (df['Estado'] == 'PE')]

print(filtro)