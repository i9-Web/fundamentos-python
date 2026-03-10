#Exemplos 7: Remover com del e pop
aluno = {"nome": "Ana", "idade": 20, "curso": "ADS", 
         "cidade": "Aracaju"}

del aluno["curso"]
cidade = aluno.pop("cidade")
print(aluno, "→ cidade removida:", cidade)
