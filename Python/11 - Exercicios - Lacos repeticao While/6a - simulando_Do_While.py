# ===============================================
# soma_positivos_pares.py
# Lê números até negativo → soma positivos e soma
# apenas os pares
# ===============================================
print("=== SOMADOR DE NÚMEROS ===")
numero = input("Digite um número ou 'S' - Para sair: ").upper()
contador = 0
soma_positivos = 0
soma_pares = 0

while numero != "S":
    if contador != 0:
        numero = input("Informe um número ou 'S' - Para sair: ").upper()
    
    if numero != "S":
        if int(numero) > 0:
            soma_positivos += int(numero)
            if int(numero) % 2 == 0:
                soma_pares += int(numero)

    contador += 1
    print(f"{contador}º iteração")
    print(f"\nSoma dos números positivos: {soma_positivos:.2f}")
    print(f"Soma dos números pares: {soma_pares:.2f}")

