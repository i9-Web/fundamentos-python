#Exemplos 2: Criar uma matriz 4x4 vazia (tudo zero)
linhas = 4
colunas = 4
matriz = []

for i in range(linhas):
    linha = [0] * colunas
    matriz.append(linha)
    
print(matriz)
