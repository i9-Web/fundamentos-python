# ===============================================
# maiorNumero.py
# Algoritmo que recebe dois números e informa qual deles
# é o maior, ou se ambos são iguais.
# ===============================================
# Entrada de dados
print("--- Maior número ---")

numero1 = int(input("Informe o primeiro número: "))
numero2 = int(input("Informe o segundo número: "))

#Processamento
if numero1 > numero2:
    print(f"O primeiro número: {numero1} é  maior que o segundo número: {numero2}. ")
elif numero1 == numero2:
    print("Os números são iguais.")
else:
    print(f"O segundo número: {numero2} é  maior que o primeiro número: {numero1} ")