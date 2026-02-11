#Coleção
palavras = ["casa", "bola", "livro", "sair", "janela"]

#Processamento: Laço de repetição "for"
for palavra in palavras:
    #Saída de dados
    if palavra == "sair":
        print("O usuário pediu para para! Prando...")
        break
    print("palavra: ", palavra)
