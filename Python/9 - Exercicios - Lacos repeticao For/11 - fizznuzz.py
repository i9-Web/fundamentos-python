#============================================================
#Algoritmo que percorra de 1 a 100 e imprima: “Fizz” se 
# divisível por 3, “Buzz” se divisível por 5, “FizzBuzz” 
# se divisível por 3 e 5 e o número em todos os outros casos.
#============================================================
print("----------- FizzBuzz de 1 a 100 -----------")
#Entrada de dados

#Processamento e saída de dados
for numero in range(1, 100):
    if numero % 3 == 0 and numero % 5 == 0:
        print("FizzBuzz")
    elif numero % 3 == 0:
        print("Fizz")
    elif numero % 5 == 0:
        print("Buzz")
    else:
        print(numero)
