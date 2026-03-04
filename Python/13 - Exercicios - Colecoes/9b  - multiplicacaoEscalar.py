#============================================================
#Elabore um programa que leia uma matriz 4×4 e faça a multiplicação
#dela por um escalar (número) informado pelo usuário. Imprima
#a matriz original e a matriz resultante.
#============================================================
#Código tradicional:
matriz = [
            [0]*4 for _ in range(4)
         ]
resultado = [
                [0]*4 for _ in range(4)
            ]

for i in range(4):
    for j in range(4):
        matriz[i][j] = int(input("Valor: "))

escalar = int(input("Multiplicador: "))

for i in range(4):
    for j in range(4):
        resultado[i][j] = matriz[i][j] * escalar

print("Matriz Original:")
for i in range(4): print(matriz[i])

print("Matriz Resultante:")
for i in range(4): print(resultado[i])
