# ===============================================
# faixaEtaria.py
# Algoritmo que lê a idade de uma pessoa e determina
# a categoria correspondente (como Primeira Infância,
# Adolescência, Meia-idade, etc.), de acordo com a tabela fornecida.
# ===============================================
# Entrada de dados (o usuário deve digitar True ou False)
print("--- Verificar faixa etária  ---")

idade = int(input("Informe a indade da pessoa (até 2 anos informe o número de dias): "))
tipo = input("A idade é em dias(d) ou am anos(a): ").lower()

if idade < 0: 
    print("A idade informada não é válida: {idade}.")
elif tipo != "d" and tipo != "a":
    print("O tipo de idade informado não é válido: {tipo}.")
else:
    if tipo == "d":
        if idade == 0:
            categoria = "Vida fetal"
        elif idade <= 28:
            categoria = "Neonatologia"
        elif idade <= 730:
            categoria = "Lactância"
        else:
            categoria = "Essa idade não é válida"
    else:
        if idade <= 2:
            categoria = "Lactância"
        elif idade <= 4:
            categoria = "Primeira Infância"
        elif idade <= 10:
            categoria = "Segunda Infância"
        elif idade <= 15:
            categoria = "Pré-adolescência"
        elif idade <= 20:
            categoria = "Adolescência"
        elif idade <= 26:
            categoria = "Pós-adolescência"
        elif idade <= 40:
            categoria = "Adultidade"
        elif idade <= 65:
            categoria = "Meia-idade"
        elif idade <= 80:
            categoria = "Terceira Idade"
        else:
            categoria = "Quarta Idade"
            
        # Saída
        print(f"Categoria: {categoria}")
