#============================================================
#Algoritmo que recebe 10 números e no final ele 
#exibe o maior número digitado
#============================================================
#Entrada de dados
maiorNumero = 0

for i in range(10):
    numero = int(input("Informe um número: "))

    if numero > maiorNumero:
        maiorNumero = numero
        print(f"Maior número atual: {maiorNumero}")

print(f"O maior número diguitado foi: {maiorNumero}")