#Exemplos 10: Set comprehension
# Set comprehension para números ímpares
numeros = range(1, 11)
impares = {x for x in numeros if x % 2 != 0}
print(f"Números ímpares: {impares}")

# Set comprehension com transformação
palavras = ["python", "java", "go", "rust"]
primeiras_letras = {palavra[0].upper() for palavra in palavras}
print(f"Primeiras letras: {primeiras_letras}")