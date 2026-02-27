#Exemplos 8: Iteração em tupla python
#Declarando um atupla de frutas 
frutas = ("maçã", "banana", "laranja", "uva")

print(f"Frutas disponíveis: {frutas}")
print(f"Frutas disponíveis:")
for i, fruta in enumerate(frutas):
    print(f"{i+1}. {fruta}")
