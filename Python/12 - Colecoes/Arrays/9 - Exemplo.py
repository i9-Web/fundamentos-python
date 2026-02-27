#Exemplos 9: Transpor matriz # (trocar linhas por colunas) → 3x4 vira 4x3
original = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

transposta = []
for j in range(len(original[0])):
    nova_linha = []
    for i in range(len(original)):
        nova_linha.append(original[i][j])
    transposta.append(nova_linha)
    print(transposta)
    transposta = []

#print("Transposta:", transposta)







