#Leita a mensagem que será repetida na tela
#Entrada de dados
mensagem = input("Digite uma mensagem: ")

repeticoes = int(input("Digite o número de repetições: "))

i = 1

while i <= repeticoes:
    print(i, " - ", mensagem)
    i += 1