#============================================================
#Algoritmo que leia o nome de um aluno e suas 4 notas, exiba
# na tela o nome e a média do aluno (A solicitação da nota deve
# ser feita usando uma das estruturas de repetição).
#============================================================
print("----------- Cáculo da média do aluno -----------")
#Entrada de dados
nome = input("Informe o nome do aluno: ")
soma = 0
contador = 1

while contador <= 4:
    nota = float(input(f"Digite a {contador}º do aluno" +  
                       "(de 0.00 até 10.00): "))
    soma += nota
    contador += 1

media = soma / 4

#Saída de dados
print("---------- Dados do aluno ----------- ")
print(f"Nome do aluno: {nome}")
print(f"Soma total das notas: {soma}")
print(f"Média do aluno: {media}")
 