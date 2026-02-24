#============================================================
#Algoritmo que que receba um número e exiba o número digitado. 
# (Esse procedimento deve acontecer pelo menos uma vez e se 
# repetir enquanto o número digitado for diferente de 0)
#============================================================
#Entrada de dados
numero = -1
while numero != 0:
    numero = int(input("Infome um número inteiro ou 0 para sair: "))
    if numero != 0:
        print(numero)
