#============================================================
#Escreva um algoritmo com uma matriz com 5 linhas e 3 colunas.
#Receba o nome, a idade e o sexo do aluno. Exiba na tela as 
#informações salvas na matriz.
#============================================================
#Código usando o potencial do Python com:
#Nested List Comprehension e .join()
matriz = [
            [input("Nome: "), 
             input("Idade: "), 
             input("Sexo: ")
            ] 
            for _ in range(5)
        ]

for aluno in matriz:
    print(" | ".join(aluno))