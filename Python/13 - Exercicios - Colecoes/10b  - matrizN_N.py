#============================================================
#Crie um algoritmo que leia uma matriz quadrada n×n (n informado
#pelo usuário) e verifique se ela é uma matriz simétrica
#(igual à sua transposta). A matriz deve ser preenchida com
#números inteiros. 
#============================================================
#Código tradicional:
linhas = int(input("Informe o número de linhas da matriz: "))
m = [
        [0]*linhas for _ in range(linhas)
    ]

for i in range(linhas):
    for j in range(linhas):
        m[i][j] = int(input("Valor: "))

eh_simetrica = True

for i in range(linhas):
    for j in range(linhas):
        if m[i][j] != m[j][i]:
            eh_simetrica = False
            break

if eh_simetrica:
    print("A matriz é simétrica.")
else:
    print("A matriz não é simétrica.")