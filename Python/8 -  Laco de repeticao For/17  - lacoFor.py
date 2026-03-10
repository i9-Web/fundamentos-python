#Coleção
nomes = [
         "Anderson", "Nathalia", "Guilerme", "Rafael", "Kaio", "Cauã",
         "Murilo", "Ana Carolina", "Kauan", "João Paulo", "Gustavo", "Thiago",
         "Maria"
         ]
#Processamento: Laço de repetição "for"
for nome in nomes:
    #Saída de dados
    if nome.startswith("K"):
        continue
    print("Nome permitido: ", nome)
