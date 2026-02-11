# ===============================================
# antecessoreSucessor.py
# Algoritmo para ler um número inteiro e mostrar
# o número, seu antecessor e seu sucessor.
# ===============================================
# 1. Leitura do número inteiro
print("--- Antecessor e Sucessor ---")
# O input() lê a entrada como string, então usamos int() para conversão (type casting)

numero = int(input("Informe um número inteiro: "))

print(f"O número digitado foi: {numero}")
print(f"O antecessor de {numero} é {numero - 1}")
print(f"O sucessor de {numero} é {numero + 1}")