#============================================================
#Escreva um algoritmo com uma matriz com 5 linhas e 2 colunas.
#Receba o nome o sexo do aluno. Exiba na tela as informações
#salvas na matriz.
#============================================================
#Código usando o potencial do Python com:
# Nested List Comprehension (ou Compreensão de Lista Aninhada) 
# combinada com Unpacking
matriz = [
            [input("Nome: "), input("Sexo (M/F): ")] for _ in range(5)
         ]

for nome, sexo in matriz:
    print(f"Nome: {nome} | Sexo: {sexo}")