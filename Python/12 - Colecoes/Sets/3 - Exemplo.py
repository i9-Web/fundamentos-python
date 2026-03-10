#Exemplos 3: Adicionando elementos ao set
frutas = {"maçã", "banana"}
print(f"Frutas após adições: {frutas}")

input("Pressione enter!")
 # Adiciona um elemento
frutas.add("laranja")
print(f"Frutas após adições: {frutas}")

# Adiciona múltiplos (maçã já existe)
input("Pressione enter!")
frutas.update(["uva", "pêra", "maçã"]) 
print(f"Frutas após adições: {frutas}")

