#============================================================
#Faça um programa que leia uma matriz 4×4 preenchida 
#pelo usuário e exiba a soma de todos os seus elementos.
#============================================================
#Código usando o portencial do Python com:
#List Comprehension e Generator Expressions.

matriz = [
            [
                int(input(f"Valor [{i}][{j}]: ")) 
                for j in range(4)
            ] 
            for i in range(4)
        ]

soma = sum(sum(linha) for linha in matriz)

print(f"Soma total dos elementos da matriz: {soma}")
