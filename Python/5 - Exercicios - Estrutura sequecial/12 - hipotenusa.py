# ===============================================
# hipotenusa.py
# Algoritmo que a partir dos catetos de um triângulo
# retângulo exiba o comprimento da hipotenusa
# (c² = a² + b²) 
# ===============================================
print("--- Cálculo da hipotenusa ---")
#Entrada de dados
cateto_oposto = float(input("Informe o comprimento do cateto opôsto: "))
cateto_adjacente = float(input("Informe o comprimento do cateto adjacente: "))
#Processamento
# 1º -Primeira forma
#soma_catetos = (cateto_oposto ** 2) + (cateto_adjacente ** 2)
#hipotenusa = soma_catetos ** 0.5
hipotenusa = ((cateto_oposto ** 2) + (cateto_adjacente ** 2)) ** 0.5
#Saída de dados
print("\n----- Resultado -----")
print(f"Cateto adjacente: {cateto_adjacente: .3f}")
print(f"Cateto opôsto: {cateto_oposto: .3f}")
print(f"O comprimento da hipotenusa é: {hipotenusa: .3f}")