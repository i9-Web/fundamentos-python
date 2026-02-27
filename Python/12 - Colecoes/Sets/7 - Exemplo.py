#Exemplos 7: Operações de diferença (difference)
cores_primarias = {"vermelho", "azul", "amarelo"}

cores_quentes = {"vermelho", "laranja", "amarelo"}
# Diferença usando - ou difference()
apenas_primarias = cores_primarias - cores_quentes

apenas_quentes = cores_quentes - cores_primarias
print(f"Cores primárias: {cores_primarias}")
print(f"Cores quentes: {cores_quentes}")

print(f"Apenas primárias: {apenas_primarias}")
print(f"Apenas quentes: {apenas_quentes}")
