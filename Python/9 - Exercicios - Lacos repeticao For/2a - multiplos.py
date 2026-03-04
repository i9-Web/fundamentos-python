#============================================================
#Algoritmo que ao receber um número inteiro, faz uma contagem
#decrescente a partir do número digitado, imprime os 10 
#primeiros múltiplos desse número e pare a execução do 
#algoritmo.
#============================================================
#Entrada de dados
numero = int(input("Infome um número inteiro: "))
contador = 1

for i in range(numero, 0, -1):
    if contador <= 10:
        if i != 0:
            if numero % i == 0:
                print(contador, " - ", i)
                contador += 1
        else:
            print("Não é possível dividir por 0")
    else:
        break