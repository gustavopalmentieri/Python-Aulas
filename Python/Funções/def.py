#FUNÇÕES EM PYTHOM SÃO BLOCOS DE CÓDIGO REUTILIZAVEIS QUE EXECUTAM TAREFAS ESPECIFICAS 
#ORGANIZANDO O PROGRAMA E EVITANDO REPTIÇÃO
#DEFINIDAS COM A PALAVRA CHAVE 'DEF', PODEM RECEBER PARÂMETROS (ENTRADAS)
#E RETORNAR O RESULTADO (SAÍDAS) COM 'RETURN'.
#TORNAM O CÓDIGO MAIS LEGIVEL, ESTRUTURADO E EFICIENTE

def saudacao(nome):  #DEF NOME (PARÂMETRO)

    return f"Olá, {nome}!" #RETORNO

mensagem = saudacao("Maria") #CHAMADA DA FUNÇÃO

print(mensagem)

#OUTRO EXEMPLO

def interacao():
    user = input("Interagi Comigo: ")
    if (user == "oi"):

        print("Olá Mundo!!")
        
    else:

        print("You is fake bro")


interacao()