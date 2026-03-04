#============================================================
#Crie um algoritmo que leia uma matriz quadrada n×n (n informado
#pelo usuário) e verifique se ela é uma matriz simétrica
#(igual à sua transposta). A matriz deve ser preenchida com
#números inteiros. 
#============================================================
#Código usando o potencial do Python com:
#Nested List Comprehensions
linhas = int(input("Informe o número de linhas da matriz: "))

m = [
        [
            int(input(f"[{i}][{j}]: ")) for j in range(linhas)
        ] 
        for i in range(linhas)
    ]

transposta = [
                list(col) for col in zip(*m)
             ]
print("Simétrica!" if m == transposta else "Não é simétrica.")
