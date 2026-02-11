# ===============================================
# autonomi.py
# algoritmo que dada uma distância percorrida 
# (em quilômetros), bem como o total de combustível
# gasto (em litros), informe o consumo médio do veículo.
# ===============================================
print("--- Autonimia do veículo ---")
#Entrada de dados 
distancia = float(input("Informe a distância percorrida (km): "))
combustivel = float(input("Informe a quantidade de combustível consumido (l): "))

#Processamento
autonomia = distancia / combustivel

#Saída de dados
print(f"Distância percorrida: {distancia}")
print(f"Combustível gasto: {combustivel}")
print(f"Consumo médio (Autonomia): {autonomia: .3f}")


