#============================================================
#Algoritmo que imprimir um losango de asteriscos com tamanho
# informado pelo usuário Exemplo com n = 5:
#============================================================
print("----------- Losango de asteriscos -----------")
#Entrada de dados
n = int(input("Digite o tamanho do losango (O número sendo ímpar fica mais bonito): "))

#Parte de cima (incluindo a linha do meio)
for i in range(1, n + 1, 2):
    espacos = " " * ((n - i) // 2)
    asteriscos = "*" * i
    print(espacos + asteriscos)

#Parte de baixo (sem repetir a linha do meio)
for i in range(n - 2, 0, -2):
    espacos = " " * ((n - i) // 2)
    asteriscos = "*" * i
    print(espacos + asteriscos)
