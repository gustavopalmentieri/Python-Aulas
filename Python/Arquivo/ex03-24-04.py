import pandas as pd 

#CAMINHO DO ARQUIVO

arquivo = 'C:/Users/Gustavo/Desktop/Área de Trabalho/AULAS/Arquivo.xlsx' #AQUI E UM CAMINHO DENTRO DA MÁQUINA PARA ENCONTRAR UM ARQUIVO EM EXCEL

#LER UMA PLANILHA ESPECÍFICA

df = pd.read_excel(arquivo, sheet_name='Plan1')

#EXIBIR INFORMAÇÕES DO DataFrame

print(df.info())