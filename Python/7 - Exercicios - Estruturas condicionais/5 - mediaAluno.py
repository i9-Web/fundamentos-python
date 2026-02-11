# ===============================================
# mediaAluno.py
# Algoritmo que lê o nome e quatro notas de um aluno,
# calcula a média e exibe a situação acadêmica:
# Reprovado (média < 5), Recuperação (5 ≤ média < 6),
# ou Aprovado (média ≥ 6).
# ===============================================
# Entrada de dados
print("--- Situação do aluno ---")
nome = input("Informe o nome do aluno: ")
nota1 = float(input(f"Informe a 1º nota do aluno {nome}: "))
nota2 = float(input(f"Informe a 2º nota do aluno {nome}: "))
nota3 = float(input(f"Informe a 2º nota do aluno {nome}: "))
nota4 = float(input(f"Informe a 4º nota do aluno {nome}: "))

#Processamento
media = (nota1 + nota2 + nota3 +nota4) / 4

if media >= 6: 
    # Saída de dados
    print(f"O aluno {nome}, encotra-se aprovado, com média: {media}")
elif media < 5:
    # Saída de dados
    print(f"O aluno {nome}, encotra-se reprovado, com média: {media}")
else:
    # Saída de dados
    print(f"O aluno {nome}, encotra-se de recuperação, com média: {media}")