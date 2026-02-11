# ===============================================
# operadorLogicoE.py
# Algoritmo que recebe duas entradas lógicas e mostra o
# resultado da operação lógica “E” (AND) entre elas.
# ===============================================
# Entrada de dados (o usuário deve digitar True ou False)
print("--- Simulação da porta lígica “E” (AND)  ---")

a = input("Digite o primeiro valor lógico (True ou False): ")
b = input("Digite o segundo valor lógico (True ou False): ")

#Processamento
if (a == "True") and (b == "True"):
    saida = True
else:
    saida = False

#Saída de dados
print(f"\nResultado da operação ({a} E {b}) = {saida}")