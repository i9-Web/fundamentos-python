#============================================================
#Elaborar um algoritmo que leia o nome de um aluno e suas
#4 notas, exiba na tela o nome e a média do aluno (A 
#solicitação da nota deve ser feita usando uma das 
# estruturas de repetição).
#============================================================
#Código usando o potencial do Python com List Comprehension:
nome = input("Nome do aluno: ")
notas = [
            float(input(f"Nota {i+1}: ")) for i in range(4)
        ]

print(f"Aluno: {nome} | Média: {sum(notas)/len(notas):.2f}")