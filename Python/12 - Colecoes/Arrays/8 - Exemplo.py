#Exemplos 8: Encontrar o maior valor da matriz
matriz = [
    [1, 2, 3, 4 ,5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

maior = matriz[0][0]
for linha in matriz:
    for valor in linha:
        if valor > maior:
            maior = valor
            
print("Maior valor =", maior)






