# ===============================================
# temperatura.py
# Algoritmo para converter uma temperatura de
# Celsius (°C) para Fahrenheit (°F).
# Fórmula: F = C * 1.8 + 32
# ===============================================
print("--- Conversor de Temperatura (°C para °F) ---")
#Entrada de dados 
# 1. Leitura da Temperatura em Celsius
temp_celsius = float(input("Digite a temperatura em graus Celsius (°C): "))

#Processamento
temp_fahrenheit = temp_celsius * 1.8 + 32

#Saída de dados 
print(f"A temperatura {temp_celsius} °C em Fahrenheit é: {temp_fahrenheit} °F ")