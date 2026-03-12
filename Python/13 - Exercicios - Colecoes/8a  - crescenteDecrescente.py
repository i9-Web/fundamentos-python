#============================================================
#Escreva um algoritmo que receba 16 números inteiros e armazene-os
#em um matriz 4 x 4. Após os números serem digitados coloque-os
#em ordem crescente. Exiba na tela a matriz em ordem em ordem
#crescente e logo em seguida em os números da matriz em ordem
#decrescente.
#============================================================
#Código usando o potencial do Python com:
#List Comprehension, a função sorted() e Slicing (Fatiamento))
# 1. Coleta de 16 números inteiros diferentes
nums_originais = []
print("Digite 16 números inteiros diferentes:")

while len(nums_originais) < 16:
    try:
        n = int(input(f"Valor {len(nums_originais) + 1}: "))
        if n not in nums_originais:
            nums_originais.append(n)
        else:
            print("Este número já foi digitado. Tente um diferente!")
    except ValueError:

# Matriz na ordem digitada
        print("Por favor, digite apenas números inteiros.")
matriz_original = [
                    nums_originais[i:i+4] for i in range(0, 16, 4)
                  ]

# Matriz em ordem crescente
nums_crescente = sorted(nums_originais)
matriz_crescente = [
                        nums_crescente[i:i+4] for i in range(0, 16, 4)
                   ]

# Matriz em ordem decrescente
nums_decrescente = nums_crescente[::-1]
matriz_decrescente = [
                        nums_decrescente[i:i+4] for i in range(0, 16, 4)
                     ]

# Função que exibi a matriz formatada
def imprimir_matriz(titulo, matriz):
    print(f"\n--- {titulo} ---")
    for linha in matriz:
        print(linha)

imprimir_matriz("Matriz original", matriz_original)
imprimir_matriz("Matriz em ordem crescente", matriz_crescente)
imprimir_matriz("Matriz em ordem decrescente", matriz_decrescente)