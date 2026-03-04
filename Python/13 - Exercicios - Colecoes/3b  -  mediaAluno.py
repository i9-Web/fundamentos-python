#============================================================
#Elaborar um algoritmo que leia o nome de um aluno e suas
#4 notas, exiba na tela o nome e a média do aluno (A 
#solicitação da nota deve ser feita usando uma das 
# estruturas de repetição).
#============================================================
#Código tradicional:
nome = input("Digite o nome: ")
notas = [0.0, 0.0, 0.0, 0.0]
soma = 0
for i in range(4):
    print("Digite a nota", i + 1, ":")
    notas[i] = float(input())
    soma = soma + notas[i]

media = soma / 4
print("Aluno:", nome)
print("Media:", media)