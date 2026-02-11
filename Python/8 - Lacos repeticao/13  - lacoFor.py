#Processamento: Laço de repetição "for"
#Dicionário
alunos = [
          {"nome: ": "Anderson", "Idade: ": 17, "Curso: ": "Técnico em informática"},
          {"nome: ": "Nathalia", "Idade: ": 17, "Curso: ": "Técnico em administração"},
          {"nome: ": "Kauan", "Idade: ": 16, "Curso: ": "Técnico em Farmácia"},
          {"nome: ": "Ana Carolina", "Idade: ": 17,"Curso: ":"Técnico em informática"}
         ]

#Processamento: Laço de repetição "for"
for aluno in alunos:
    #Saída de dados
    for chave, valor in aluno.items():
        print(chave, ": ", valor)


