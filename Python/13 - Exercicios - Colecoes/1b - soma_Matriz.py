#============================================================
#Faça um programa que leia uma matriz 4×4 preenchida 
#pelo usuário e exiba a soma de todos os seus elementos.
#============================================================
#Código tradicional
matriz = [
            [0,0,0,0], 
            [0,0,0,0], 
            [0,0,0,0], 
            [0,0,0,0]
         ]
for i in range(4):
    for j in range(4):
        matriz[i][j] = int(input("Digite o valor: "))

soma = 0
for i in range(4):
    for j in range(4):
        soma = soma + matriz[i][j]
print("Soma total:", soma)