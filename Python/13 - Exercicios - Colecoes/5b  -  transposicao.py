#============================================================
#Desenvolva um algoritmo com duas matrizes 4 x 4. Receba 16
#números diferentes e armazene na primeira matriz (preencha-a
#linha a linha). Ao final da digitação transfira os elementos
#da primeira matriz para segunda, sendo que os números das
#linhas devem ir para as colunas e vice-versa. Após o último
#procedimento exiba na tela as duas matrizes lado a lado.
#============================================================
#Código tradicional:
m1 = [
        [0]*4 for _ in range(4)
     ]
m2 = [
        [0]*4 for _ in range(4)
     ]

for i in range(4):
    for j in range(4):
        m1[i][j] = int(input("Valor: "))

for i in range(4):
    for j in range(4):
        m2[j][i] = m1[i][j]

for i in range(4):
    print(m1[i], "   ", m2[i])