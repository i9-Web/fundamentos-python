#===============================================
# trocaDeOleo.py
# Algoritmo que, dado a quilometragem da última troca
# de óleo e filtro, informa se deve ser feita apenas a
# troca de óleo ou a troca de óleo mais o filtro.
# ===============================================
# Entrada de dados
print("--- Troca de óleo ---")
km_anterior = float(input("Informe a quilometragem anterior: "))
km_atual = float(input("Informe a quilometragem atual: "))

#Processamento
distancia_percorrida = km_atual - km_anterior


if distancia_percorrida >= 15000:
    #Saída de dados
    print(f"É necessário trocar o óleo e o filtro.\n Pois, a distência percorrida foi de {distancia_percorrida} km")
else:
    #Saída de dados
    print(f"Troque apenas o óleo.\n Pois, a distência percorrida foi de {distancia_percorrida} km")