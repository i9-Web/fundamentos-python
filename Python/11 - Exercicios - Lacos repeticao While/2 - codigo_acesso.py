#============================================================
#Algoritmo que peça o código de acesso ao usuário enquanto o 
# código digitado for diferente do código de controle(123456)
#============================================================
print("----------- Sistema de controle de acesso -----------")
#Entrada de dados
CODIGO_ACESSO = 123456

while True:
    codigo = int(input("Digite o código de acesso: "))

    if codigo == CODIGO_ACESSO:
        print("Acesso liberado! Bem-vindo!")
        break
    else: 
        print("Código INCORRETO! Tente novamente.\n")