#Exemplos 11: Frozen set (set imutável)
# FrozenSet - versão imutável do set
cores_basicas = frozenset(["vermelho", "verde", "azul"])

print(f"FrozenSet: {cores_basicas}")
print(f"Tipo: {type(cores_basicas)}")
# Pode ser usado como chave de dicionário
paletas = {
        cores_basicas: "RGB",
        frozenset(["cyan", "magenta", "yellow"]): "CMY"
}

print(f"Paletas: {paletas}")