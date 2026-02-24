# ===============================================
# calculadora_while.py
# Calculadora simples com repetição usando while
# ===============================================
print("=== CALCULADORA INTERATIVA ===")
print("Digite 'sair' a qualquer momento para encerrar.\n")
while True:
    operador = input("Operador (+, -, *, /): ")

    if operador.lower() == "sair":
        print("Encerrando a calculadora.")
        break

    if operador not in ['+', '-', '*', '/']:
        print("Operador inválido! Tente novamente.\n")
        continue

    n1 = input("Digite o primeiro número: ")
    if n1.lower() == "sair": break
    
    n2 = input("Digite o segundo número: ")
    if n2.lower() == "sair": break

    n1 = float(n1)
    n2 = float(n2)

    if operador == '+':
        resultado = n1 + n2
    elif operador == '-':
        resultado = n1 - n2
    elif operador == '*':
        resultado = n1 * n2
    elif operador == '/':
        if n2 == 0:
            print("Erro: divisão por zero!\n")
            continue
        resultado = n1 / n2
    print(f"Resultado: {n1} {operador} {n2} = {resultado}\n")