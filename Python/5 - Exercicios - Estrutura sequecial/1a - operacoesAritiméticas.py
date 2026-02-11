# ===============================================
# operacoesAritmeticas.py
# Algoritmo que ler dois números inteiros e realiza
# as operações aritméticas básicas.
# ===============================================
# 1. Leitura dos números inteiros
print("--- Calculadora Simples ---")

k = int(input("Informe o primeiro número inteiro: "))
j = int(input("Informe o segundo número inteiro: "))

resultado = k + j
print(f"A soma de {k} + {j} = {resultado}")
resultado = k - j
print(f"A subtração de {k} - {j} = {resultado}")
resultado = k / j
print(f"A divisão de {k} / {j} = {resultado}")
resultado = k // j
print(f"A divisão inteira de {k} // {j} = {resultado}")
resultado = k % j
print(f"O resto da divisão de {k} % {j} = {resultado}")
resultado = k * j
print(f"A multiplicação de {k} * {j} = {resultado}")
resultado = k ** j
print(f"{k} elevado {j} = {resultado}")
