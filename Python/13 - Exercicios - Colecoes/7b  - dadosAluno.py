#============================================================
#Escreva um algoritmo com uma matriz com 5 linhas e 3 colunas.
#Receba o nome, a idade e o sexo do aluno. Exiba na tela as 
#informações salvas na matriz.
#============================================================
#Código tradicional:
matriz = [
            ["", "", ""] 
            ["", "", ""] #for _ in range(5)
            ["", "", ""] #for _ in range(5)
            ["", "", ""] #for _ in range(5)
            ["", "", ""] #for _ in range(5)
         ]
for i in range(5):
    matriz[i][0] = input("Nome: ")
    matriz[i][1] = input("Idade: ")
    matriz[i][2] = input("Sexo: ")

for i in range(5):
    print("Dados:", matriz[i][0], matriz[i][1], matriz[i][2])