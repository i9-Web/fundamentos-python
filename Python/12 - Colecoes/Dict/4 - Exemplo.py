#Exemplos 4: Acessar valor (ou tratar chave inexistente)
aluno = {"nome": "Ana", "idade": 20, "curso": "ADS"}

print(aluno["nome"])     

# valor padrão
print(aluno.get("cidade", "Não informado")) 
