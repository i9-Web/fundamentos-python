#Exemplos 10: Contador de letras
frase = "python é legal de mais"
contagem = {}
for letra in frase:
    if letra != " ":
        contagem[letra] = contagem.get(letra, 0) + 1

print(contagem)  




