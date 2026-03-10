# ===============================================
# soma_positivos_pares.py
# Lê números até negativo → soma positivos e soma
# apenas os pares
# ===============================================
print("=== SOMADOR DE NÚMEROS ===")
soma = 0
soma_pares = 0

while True:
    numero = int(input("Informe um número positivo " +
                   "ou número negativo para sair: "))
    if numero >= 0:
        soma += numero
        if numero % 2 == 0:
            soma_pares += numero
    else:
        break

print(f"\nSoma dos números positivos: {soma:.2f}")
print(f"Soma dos números pares: {soma_pares:.2f}")

