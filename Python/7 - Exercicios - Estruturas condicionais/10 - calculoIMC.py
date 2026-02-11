# ===============================================
# calculoIMC.py
# Algoritmo que calcula o IMC de uma pessoa a partir do
# peso e altura, e informa a condição (Abaixo do peso,
# Peso ideal, Sobrepeso, Obesidade Grau I ou Obeso)
# conforme o sexo e a tabela de referência.
# ===============================================
# Entrada de dados (o usuário deve digitar True ou False)
print("--- Calculadora do IMC  ---")
# Entrada de dados
sexo = input("Digite o sexo (M - para masculino, F - para feminino): ").upper()
peso = float(input("Informe seu peso (em kg): "))
altura = float(input("Informe sua altura (em metros): "))

# Cálculo do IMC
imc = peso / (altura ** 2)

# Determinação da condição com base no sexo
if sexo == "F":
    if imc < 19.1:
        condicao = "Abaixo do peso"
    elif imc <= 25.8:
        condicao = "Peso ideal"
    elif imc <= 27.3:
        condicao = "Sobrepeso"
    elif imc <= 32.3:
        condicao = "Obesidade Grau I"
    else:
        condicao = "Obeso"
elif sexo == "M":
    if imc < 20.7:
        condicao = "Abaixo do peso"
    elif imc <= 26.4:
        condicao = "Peso ideal"
    elif imc <= 27.8:
        condicao = "Sobrepeso"
    elif imc <= 31.1:
        condicao = "Obesidade Grau I"
    else:
        condicao = "Obeso"
else:
    condicao = "Sexo inválido!"
    
# Saída
print(f"\nIMC = {imc:.2f}")
print(f"Condição: {condicao}")