# ===============================================
# media.py
# Algoritmo que leia o nome de um aluno e suas 4 
# notas, exiba na tela o nome e a média do aluno.
# ===============================================
print("--- Custo da Obra ---")
#Entrada de dados 
nome = input("informe o nome do aluno: ")
nota1 = float(input("Informe a primeira nota do aluno: "))
nota2 = float(input("Informe a segunda nota do aluno: "))
nota3 = float(input("Informe a terceira nota do aluno: "))
nota4 = float(input("Informe a quarta nota do aluno: "))

#Processamento
media = (nota1 + nota2 + nota3 + nota4) / 4

#Saída de dados
print(f"O aluno {nome} tem a média {media: .2f}")