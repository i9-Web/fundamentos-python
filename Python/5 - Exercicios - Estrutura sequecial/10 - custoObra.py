# ===============================================
# custoObra.py
# algoritmo que calcule quantos metros quadrados 
# de gesso são necessários para forrar um ambiente. 
# Exiba na tela, de forma discrimina, quanto vai 
# custa a obra. Levando em conta o valor do metro 
# quadrado do gesso e da mão de obra para aplicação
# (A aplicação é cobrada por M^2)
# ===============================================
print("--- Custo da Obra ---")
#Entrada de dados 
largura = float(input("Infome a LARGURA do ambiente (em metros): "))
comprimento = float(input("Infome o COMPRIMENTO do ambiente (em metros): "))
preco_material_m2 = float(input("Informe o preço do m² do GESSO: R$ "))
preco_mao_obra_m2 = float(input("Informe o preço da MÃO DE OBRA por m²: R$ "))

#Processamento
area_total_m2 = largura * comprimento
valor_total_material = preco_material_m2 * area_total_m2
valor_total_mao_obra = preco_material_m2 * area_total_m2
custo_total_obra = valor_total_material + valor_total_mao_obra

#Saída de dados
print("\n" + "=" * 50)
print(" " * 15 + "ORÇAMENTO DA OBRA")
print("\n" + "=" * 50)
print("\n [DADOS do AMBIENTE]")
print(f"Largura:     {largura: .2f} m²")
print(f"Comprimento: {comprimento: .2f} m²")
print(f"Área total:  {area_total_m2: .2f} m²")
print("\n [CUSTO POR M²]")
print(f"Custo do material por m²: R$ {valor_total_material}")
print(f"Custo da mão de obra por m²: R$ {valor_total_mao_obra}")
print(f"-" * 30)
print(f"Total da obra: R$ {custo_total_obra}")
print("\n" + "=" * 50)