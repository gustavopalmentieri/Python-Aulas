usuario = ''
senha = ''
tentativas = 0

while (usuario != 'gustavo' and senha != 'senha123') and tentativas < 3: 

    usuario = input('Digite o seu usuário: ')
    senha = input('Digite sua senha: ')
    tentativas = tentativas + 1

    if usuario != 'gustavo' and senha != 'senha123':

        print('Aguarde: 30 minutos e tente novamente!!')
    
    else:

        print('Login Efetuado com Sucesso!!')