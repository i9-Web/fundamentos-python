# ===============================================
# novoSalario.py
# Algoritmo para calcular o novo salário com base
# em um percentual de aumento.
# Exiba na tela o nome do funcionário e o seu novo 
# salário.
# ===============================================
# Entrada de dados
print("--- Calculadora de Novo Salário ---")
# 1. Leitura do Nome do Funcionário (String)
nome_funcionario = input("Digite o nome do funcionário: ")
# 2. Leitura do Salário Atual (Float)
salario_atual = float(input("Digite o salário atual (ex: 2500.50): "))
# 3. Leitura do Percentual de Aumento
percentual_aumento = float(input("Digite o percentual de aumento (ex: 10 para 10%): "))

# Processamento dos dados 
#1º - Forma para calcular o salário
novo_salario1 = salario_atual + ((salario_atual * percentual_aumento) / 100) 
#2º - Forma para calcular o salário
novo_salario2 = salario_atual + ((percentual_aumento / 100) * salario_atual)
#3º - Forma para calcular o salário
novo_salario3 = salario_atual + ((salario_atual / 100) * percentual_aumento)  

# Saída de dados
print(f"O fubncionário {nome_funcionario}, passou a receber R$ {novo_salario1} ")
print(f"O fubncionário {nome_funcionario}, passou a receber R$ {novo_salario2} ")
print(f"O fubncionário {nome_funcionario}, passou a receber R$ {novo_salario3} ")

