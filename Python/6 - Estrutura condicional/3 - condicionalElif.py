#Entrada de dados: Recebe um número inteiro
media = float(input("Digite a media do aluno: "))

#Processamento: Teste condicional
if media >= 9:
    #Saída de dados
    print("Aprovado com distinção! Excelente trabalho.")
elif media >= 6:
    #Saída de dados
    print("Aprovado! Bom trabalho.")
elif media >= 5:
    #Saída de dados
    print("Em recuperação. Você precisa estudar mais.")
else:
    #Saída de dados
    print("Reprovado. Vamos tentar novamente no próximo semestre.")
