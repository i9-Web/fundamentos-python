# ===============================================
# lojaDVD.py
# Algoritmo que calcula o valor total da compra de DVDs.
# Cada DVD custa R$ 1,50, mas se forem comprados 10 ou
# mais unidades, o preço cai para R$ 1,17.
# ===============================================
# Entrada de dados
print("--- Loja de conveniência ---")

quant_dvd = int(input("Informe a quantidade de DVD's: "))

#Processamento
if quant_dvd >= 10:
    preco = 1.17
else: 
    preco = 1.5

total = quant_dvd * preco

#Saída de dados
print(f"Total da compra : R$ {total}.\n Preço por DVD R$ {preco}.")
