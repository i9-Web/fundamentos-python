#Exemplos 5: Operações de união (union)
frutas_tropicais = {"manga", "abacaxi", "coco"}

frutas_citrus = {"laranja", "limão", "tangerina"}

# União usando | ou union()
todas_frutas = frutas_tropicais | frutas_citrus
todas_frutas2 = frutas_tropicais.union(frutas_citrus)

print(f"Frutas tropicais: {frutas_tropicais}")
print(f"Frutas cítricas: {frutas_citrus}")
print(f"Todas as frutas: {todas_frutas}")
print(f"Todas as frutas: {todas_frutas2}")
