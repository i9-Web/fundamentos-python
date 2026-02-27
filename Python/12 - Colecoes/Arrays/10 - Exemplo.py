#Exemplos 10: Multiplicar todos os elementos por 2
matriz = [
[1, 2, 3, 4 ,5],
[6, 7, 8, 9, 10],
[11, 12, 13, 14, 15]
]
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        matriz[i][j] *= 2
        
print("Matriz dobrada:", matriz)







