#Exemplo de While com else: Executa o laço normalmente e, 
#como não houve break, o bloco else é executado ao final
#Entrada de dados
cont = 1

while cont <= 15:
    print(cont)
    cont += 1
else:
    print("While terminou normalmente")
    