# ===============================================
# lojaDVD.py
# Algoritmo que calcula o valor total da compra de DVDs.
# Cada DVD custa R$ 1,50, mas se forem comprados 10 ou
# mais unidades, o preço cai para R$ 1,17.
# ===============================================
# Entrada de dados
print("--- Loja de conveniência ---")

quant_dvd = int(input("Informe a quantidade de DVD's: "))

if quant_dvd >= 10:
    #Saída de dados com processamento
    print(f"Total da compra : R$ {quant_dvd * 1.17}.\n Preço por DVD R$ 1,17.")
else:
        #Saída de dados com processamento
    print(f"Total da compra : R$ {quant_dvd * 1.5}.\n Preço por DVD R$ 1,50.")
