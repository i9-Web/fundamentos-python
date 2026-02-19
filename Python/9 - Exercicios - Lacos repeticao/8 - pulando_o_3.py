#============================================================
#Algoritmo que imprime os números de 1 até 100, mas pule 
# qualquer número que contenha o dígito “3” (ex: 3, 13, 23,
# 30).
#============================================================
print("----------- Número de 1 até 100 (sem o dígito 3) -----------")

for numero in range(1, 101):
    if "3" in str(numero):
        continue
    print(numero)
    