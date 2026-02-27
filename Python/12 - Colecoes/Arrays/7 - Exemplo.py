#Exemplos 7: Somar todos os elementos da matriz
matriz = [
    [1, 2, 3, 4 ,5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]
soma = 0
for linha in matriz:
    for valor in linha:
        soma += valor
print("Soma total =", soma)





