# ===============================================
# trocarValores.py
# Algoritmo que leia dois valores inteiros e efetue
# a troca desses valores nas suas respectivas variáveis.
# Imprima na tela os valores invertidos.
# ===============================================
print("--- Trocar valores das variávies ---")
#Entrada de dados 
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
temporario = 0

#Processamento
temporario = numero1
numero1 = numero2
numero2 = temporario

#Saída de dados
print(f"O valor guardado na variável 1 é: {numero1}")
print(f"O valor guardado na variável 2 é: {numero2}")