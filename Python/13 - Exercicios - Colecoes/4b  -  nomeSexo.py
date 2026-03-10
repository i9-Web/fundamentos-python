#============================================================
#Escreva um algoritmo com uma matriz com 5 linhas e 2 colunas.
#Receba o nome o sexo do aluno. Exiba na tela as informações
#salvas na matriz.
#============================================================
#Código tradicional:
matriz = [
            ["", ""], 
            ["", ""], 
            ["", ""], 
            ["", ""], 
            ["", ""]
        ]
for i in range(5):
    matriz[i][0] = input("Digite o nome: ")
    matriz[i][1] = input("Digite o sexo: ")

for i in range(5):
    print("Nome:", matriz[i][0], "- Sexo:", matriz[i][1])