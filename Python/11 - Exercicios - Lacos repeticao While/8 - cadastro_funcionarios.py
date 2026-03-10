# ==========================================================
# cadastro_funcionarios.py
# Cadastro de funcionários com relatório final usando while
# ==========================================================
print("=== CADASTRO DE FUNCIONÁRIOS ===")
print("Digite 'sair' no nome para encerrar o cadastro.\n")
qtd = 0
soma_salarios = 0
mais_velho_nome = ""
mais_velho_idade = -1
maior_salario_nome = ""
maior_salario_valor = -1

while True:
    nome = input("Nome do funcionário: ")
    if nome.lower() == "sair":
        print("\nEncerrando cadastro...\n")
        break
    sexo = input("Sexo (M/F): ")
    idade = int(input("Idade: "))
    salario = float(input("Salário: "))
    print("-------------------------------------")
    qtd += 1
    soma_salarios += salario

    # Verifica mais velho
    if idade > mais_velho_idade:
        mais_velho_idade = idade
        mais_velho_nome = nome

    # Verifica maior salário
    if salario > maior_salario_valor:
        maior_salario_valor = salario
        maior_salario_nome = nome
    # ====== RELATÓRIO FINAL ======
print("=========== RELATÓRIO FINAL ===========")
print(f"Total de funcionários cadastrados: {qtd}")
if qtd > 0:
    media_salarios = soma_salarios / qtd
    print(f"Média dos salários: R$ {media_salarios:.2f}")
    print(f"Funcionário mais velho: {mais_velho_nome} {mais_velho_idade} anos")
    print(f"Maior salário: {maior_salario_nome} (R$ {maior_salario_valor:.2f})")
else:
    print("Nenhum funcionário foi cadastrado.")
print("========================================")