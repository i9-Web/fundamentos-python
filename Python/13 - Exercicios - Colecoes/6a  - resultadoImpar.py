#============================================================
#Crie um algoritmo que contenha uma matiz 5 x 3 e preencha-a
#com números inteiros. Exiba na tela os números da linha da
#matriz cujo a soma resulte em um número ímpar.
#============================================================
#Código usando o potencial do Python com:
#List Comprehension.
matriz = [
                [int(input(f"V[{i}][{j}]: ")) for j in range(3)] 
                for i in range(5)
         ]
[
    print(linha) for linha in matriz if sum(linha) % 2 != 0
]