# ===============================================
# combustivelVantajoso.py
# Algoritmo que compara o preço do álcool e da gasolina
# e informa qual é mais vantajoso abastecer.
# É vantagem usar álcool se custar até 70% do preço da gasolina.
# ===============================================
# Entrada de dados
print("--- Álcool ou Gasolina ---")
preco_Alcool = float(input("Informe o preço do Álcool: R$ "))
preco_Gasolina = float(input("Informe o preço do Gasolina: R$ "))

percentual =  (preco_Alcool / preco_Gasolina) * 100

if percentual <= 70:
    print(f"É mais vantajoso abastecer com Álcool, pois, representa {percentual: .2f} % do preço da Gasolina.")
else:
    print(f"É mais vantajoso abastecer com Gasolina, pois, o Álcool representa {percentual: .2f} % do preço da Gasolina.")

