# ===============================================
# imc.py
# Algoritmo para calcular e exibir o IMC de uma pessoa.
# Fórmula: IMC = Peso / (Altura * Altura)
# ===============================================
print("--- Calculadora de IMC (Índice de Massa Corporal) ---")
# 1. Leitura do peso é em quilogramas (float para aceitar valores decimais)
peso_kg = float(input("Digite o peso em quilogramas (ex: 75.5): "))
# 2. Leitura da altura é em metros (float para aceitar valores decimais)
altura_m = float(input("Digite a altura em metros (ex: 1.75): "))

#Processamento de dados
#imc = peso_kg / (altura_m ** 2)
imc = peso_kg / (altura_m * altura_m)

#Saída de dados
print(f"O seu IMC é: {imc}")
