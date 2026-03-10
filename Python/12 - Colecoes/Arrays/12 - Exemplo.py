#Exemplos 12: Somar duas matrizes do mesmo tamanho
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
C = []
for i in range(len(A)):
    linha = []
    for j in range(len(A[i])):
        linha.append(A[i][j] + B[i][j])
    C.append(linha)
print("A + B =", C)










