# ===============================================
# tratamentoNome.py
# Algoritmo que lê o nome e o sexo de uma pessoa e exibe
# o nome precedido do pronome de tratamento “Sr.” ou “Sra.”.
# ===============================================
print("--- Pronome de tratamento  ---")

#Entrada de dados
nome = input("Informe seu nome: ")
sexo = input("Informe seu sexo (M - Masculino ou F - Feminino): ").upper()

#Processamento
if sexo == "M":
    print(f"Sr. {nome}")
elif sexo == "F":
    print(f"Srª. {nome}")
else:
    print("Sexo inválido! Digite apenas 'M' para masculino ou 'F' para feminino.")



