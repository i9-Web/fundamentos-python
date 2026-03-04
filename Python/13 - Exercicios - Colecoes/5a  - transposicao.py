#============================================================
#Desenvolva um algoritmo com duas matrizes 4 x 4. Receba 16
#números diferentes e armazene na primeira matriz (preencha-a
#linha a linha). Ao final da digitação transfira os elementos
#da primeira matriz para segunda, sendo que os números das
#linhas devem ir para as colunas e vice-versa. Após o último
#procedimento exiba na tela as duas matrizes lado a lado.
#============================================================
#Código usando o potencial do Python com:
#Nested List Comprehension e Unpacking Operator (*) combinado 
#com a função zip().
m1 = [
        [int(input(f"L{i}C{j}: ")) for j in range(4)] for i in range(4)
     ]
m2 = [
        list(coluna) for coluna in zip(*m1)
     ]

for r1, r2 in zip(m1, m2):
    print(f"{r1} \t {r2}")