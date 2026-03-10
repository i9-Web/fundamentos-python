#============================================================
#Algoritmo que usando um único for com range, calcule e 
# imprima a soma de todos os números ímpares de 0 até 100.
#============================================================
print("----------- Some os número ímpares de 0 até 100 -----------")
soma = 0

#2º - Forma
for numero in range(1, 101, 2):
        soma += numero
print(soma)