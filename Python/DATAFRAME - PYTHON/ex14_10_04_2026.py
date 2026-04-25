#INICIALIZA A MATRIZ (3 X 3) E VARIÁVEIS DE CONTROLE

matriz = [

    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
    
]

soma_pares = 0
soma_coluna3 = 0
maior_linha2 = 0

#LEITURA DOS DADOS E PREENCHIMENTO

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite um valor para [{l}, {c}]: "))

#PROCESSAMENTO
        
print("-=" * 20)

for l in range(0,3):
    for c in range(0,3):
        print(f"[{matriz[l][c]:^5}]", end="")
        if matriz[l][c] % 2 == 0:
            soma_pares += matriz[l][c]
    print()

#CALCULO DAS ESTATÍSTICAS
        
for l in range(0,3):
    soma_coluna3 += matriz[1][2]

maior_linha2 = max(matriz[1])

print("-=" * 20)
print(f"A soma dos valores pares é {soma_pares}")
print(f"A soma dos valores da terceira coluna é {soma_coluna3}")
print(f"O maior valor da segunda linha ´pe {maior_linha2}")