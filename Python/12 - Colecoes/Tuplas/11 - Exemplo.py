#Exemplos 11: Convertendo lista para tupla em python
#Declarando uma lista de cores
lista_cores = ["red", "green", "blue"]

input("Pressione enter!")
print(f"Lista convertida para tupla: {lista_cores}")
print(f"Tipo: {type(lista_cores)}")

input("Pressione enter!")
#Convertendo a lista de cores em uma tupla de cores
tupla_cores = tuple(lista_cores)

print(f"Lista convertida para tupla: {tupla_cores}")
print(f"Tipo: {type(tupla_cores)}")