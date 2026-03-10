#============================================================
#Crie um algoritmo que contenha uma matiz 5 x 3 e preencha-a
#com números inteiros. Exiba na tela os números da linha da
#matriz cujo a soma resulte em um número ímpar.
#============================================================
#Código tradicional:
matriz = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
for i in range(5):
    for j in range(3):
        matriz[i][j] = int(input("Digite: "))

for i in range(5):
    soma_linha = 0
    for j in range(3):
        soma_linha += matriz[i][j]
    
    if soma_linha % 2 != 0:
        for j in range(3):
            print(matriz[i][j], end=" ")
        print(" = ", soma_linha)