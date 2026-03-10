#============================================================
#Elabore um programa que leia uma matriz 4×4 e faça a multiplicação
#dela por um escalar (número) informado pelo usuário. Imprima
#a matriz original e a matriz resultante.
#============================================================
#Código usando o potencial do Python com:
#Nested List Comprehensions
matriz = [
            [
                int(input(f"V[{i}][{j}]: ")) for j in range(4)
            ] 
            for i in range(4)
         ]

escalar = int(input("Escalar: "))

resultado = [
                [val * escalar for val in linha] 
                for linha in matriz
            ]
print(f"Original: {matriz}\nResultante: {resultado}")