#Exemplos 9: Percorrer chaves, valores e itens
aluno = {"nome": "Ana", "idade": 20, "curso": "ADS", 
         "cidade": "Aracaju"}

print("Chaves:", list(aluno.keys()))
print("Valores:", list(aluno.values()))

for chave, valor in aluno.items():
    print(f"{chave}: {valor}")



