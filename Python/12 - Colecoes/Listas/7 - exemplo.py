#xemplos 7: List comprehension - números pares.
#Declarando a lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Números pares: {numeros}")

input("Pressione enter!")
pares = [x for x in numeros if x % 2 == 0]
print(f"Números pares: {pares}")

input("Pressione enter!")
impares = [y for y in numeros if y % 2 != 0]
print(f"Números ímpares: {impares}")