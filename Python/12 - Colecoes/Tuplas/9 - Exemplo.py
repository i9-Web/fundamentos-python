#Exemplos 9: Tupla como chave de dicionário pytho
# Tuplas são imutáveis, então podem ser chaves 
# de dicionários
#Declarando um atupla de pontos no plano cartezeano 
pontos = {
    (0, 0): "origem",
    (1, 1): "diagonal",
    (0, 1): "eixo y",
    (1, 0): "eixo x"
}

print(f"Ponto (1, 1): {pontos[(1, 1)]}")
print(f"Todos os pontos: {pontos}")
