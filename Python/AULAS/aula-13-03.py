#CONDIÇÕES ENCADEADAS (IF, ELIF E ELSE) - AULA DE SEXTA-FEIRA

atrasos = int(input('Quantas faltas ou atrasos você tem? '))

if atrasos >= 3:

    print('Você está suspenso')

elif atrasos == 2:

    print('Mais uma falta, você estará suspenso!')

elif atrasos == 1:

    print('Mais duas faltas e estará suspenso!')

else:

    print('Pode entrar!!') 