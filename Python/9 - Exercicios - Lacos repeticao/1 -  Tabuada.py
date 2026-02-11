#============================================================
#Algoritmo que imprime na tela a tabuada de multiplicação
#de um número inteiro digitado pelo usuário.
#============================================================
#Entrada de dados
numero = int(input("Infome um número inteiro: "))

#Processamento e saída dos dados
for i in range(11):
    print(f"{numero} x {i} = {numero * i }")