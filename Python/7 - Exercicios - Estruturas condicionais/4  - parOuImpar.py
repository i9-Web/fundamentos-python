# ===============================================
# parOuImpar.py
# Algoritmo que recebe um número inteiro e informa se ele
# é par ou ímpar.
# ===============================================
# Entrada de dados
print("--- Loja de conveniência ---")

numero = int(input("Digite um número: "))

#Processamento
if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")