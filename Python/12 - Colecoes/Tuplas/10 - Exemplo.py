#Exemplos 10: Usando função para retornar múltiplos 
# valores (usando tupla) em python.
def calcular_estatisticas(numeros):
    """Retorna média, maior e menor valor"""
    media = sum(numeros) / len(numeros)
    maximo = max(numeros)
    minimo = min(numeros)

    # Retorna uma tupla
    return media, maximo, minimo 

# Usando a função
valores = [10, 20, 30, 40, 50]
media, maior, menor = calcular_estatisticas(valores)
print(f"Média: {media}")
print(f"Maior: {maior}")
print(f"Menor: {menor}")