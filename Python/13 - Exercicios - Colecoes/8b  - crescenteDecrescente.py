#============================================================
#Escreva um algoritmo que receba 16 números inteiros e armazene-os
#em um matriz 4 x 4. Após os números serem digitados coloque-os
#em ordem crescente. Exiba na tela a matriz em ordem em ordem
#crescente e logo em seguida em os números da matriz em ordem
#decrescente.
#============================================================
#Código tradicional:

vetor = [0] * 16

for i in range(16):
    vetor[i] = int(input("Digite: "))

# Bubble Sort (Tradicional)
for i in range(16):
    for j in range(0, 16 - i - 1):
        if vetor[j] > vetor[j + 1]:
            temp = vetor[j]
            vetor[j] = vetor[j+1]
            vetor[j+1] = temp

# Matriz Crescente
print("Matriz Crescente:")
for i in range(4):
    for j in range(4):
        print(vetor[i*4 + j], end=" ")
    print()

# Matriz Decrescente
print("Matriz Decrescente:")
for i in range(3, -1, -1):
    for j in range(3, -1, -1):
        print(vetor[i*4 + j], end=" ")
    print()
