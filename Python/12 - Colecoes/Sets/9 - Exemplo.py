#Exemplos 9: Verificações de pertencimento e subconjuntos
numeros_pares = {2, 4, 6, 8, 10}
numeros_pequenos = {2, 4}
numeros_grandes = {100, 200}
# Verificar se é um elemento do conjunto
print(f"4 está em pares? {4 in numeros_pares}")
print(f"3 está em pares? {3 in numeros_pares}")
# Verificar subconjunto
print("O conjuto dos números pequenos é subconjunto dos pares?") 
print(f"{numeros_pequenos.issubset(numeros_pares)}")
print("O conjuto dos números pares é superconjunto dos pequenos")  
print(f"{numeros_pares.issuperset(numeros_pequenos)}")
# Verificar se são disjuntos (sem elementos em comum)
print(f"O conjuto dos números pares e o conjuto dos números" + 
        "grandes são disjuntos?") 
print(f"{numeros_pares.isdisjoint(numeros_grandes)}")



