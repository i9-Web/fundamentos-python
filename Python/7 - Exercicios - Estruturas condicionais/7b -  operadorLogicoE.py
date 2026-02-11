# ===============================================
# operadorLogicoE.py
# Algoritmo que recebe duas entradas lógicas e mostra o
# resultado da operação lógica “E” (AND) entre elas.
# ===============================================
# Entrada de dados (o usuário deve digitar True ou False)
print("--- Simulação da porta lígica “E” (AND)  ---")

a = int(input("Digite o primeiro valor lógico (1 - True ou 0 - False): "))
b = int(input("Digite o segundo valor lógico (1 - True ou 0 - False): "))


#Saída de dados
print(f"\nResultado da operação ({a} E {b}) = {a * b}")