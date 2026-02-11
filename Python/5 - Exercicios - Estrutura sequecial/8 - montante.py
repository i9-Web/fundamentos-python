# ===============================================
# montante.py
# Dados um capital C, uma taxa de juros mensal fixa
#J e um período de aplicação em meses M, informe o
#montante F no final do período (F=C*(1+J/100)^M). 
# ===============================================
print("--- Calcular montante final ---")
#Entrada de dados 
capital = float(input("Informe o capital inicial: R$ "))
juros_mensal = float(input("Informe a taxa de juros mensal (%): "))
meses = float(input("Informe o período de aplicação em meses: "))

#Processamento
valor_final = capital * ((1+ (juros_mensal/100)) ** meses)

#Saída de dados 
print(f"O montante final para o período de {meses} meses é {valor_final: .00f}")
