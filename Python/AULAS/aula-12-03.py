idades = ['18', '21', '16', '30', '42', '19']
menor_idade = []
maior_idade = []


for idade in idades:

    if idade < '18':

        menor_idade.append(idade)

    
    else:

        maior_idade.append(idade)


print('Lista dos menores de idade: ', menor_idade)
print('Lista dos maiores de idade: ', maior_idade)