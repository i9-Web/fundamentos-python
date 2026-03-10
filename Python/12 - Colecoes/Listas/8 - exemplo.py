#Exemplos 8: List comprehension avançada - filtrar e transformar strings
#Declarando a lista de palavras
palavras = ["python", "java", "javascript", "go", "rust"]
print(f"Lista de palavras: {palavras}")

input("Pressione enter!")
# Apenas palavras com mais de 4 letras, em maiúsculo
palavras_longas = [x.upper() for x in palavras if len(x) > 4]

print(f"Palavras longas em maiúsculo: {palavras_longas}")

print(f"Tipo: {type(palavras)}")


