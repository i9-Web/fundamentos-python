#============================================================
#Algoritmo que usando o laço for, imprima os números pares de
# 0 até 30. 
#============================================================
print("----------- Números pares de 0 até 30 -----------")

#1º - Forma
for numero in range(0, 31):
    if numero % 2 == 0:
       print(numero)