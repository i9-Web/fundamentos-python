# Simulando dados de visitantes de um site
visitantes_janeiro = {"user1", "user2", "user3", "user4", "user5"}
visitantes_fevereiro = {"user3", "user4", "user5", "user6", "user7"}
visitantes_marco = {"user1", "user5", "user6", "user8", "user9"}
# Análises
todos_visitantes = visitantes_janeiro | visitantes_fevereiro | visitantes_marco
visitantes_fieis = visitantes_janeiro & visitantes_fevereiro & visitantes_marco
novos_fevereiro = visitantes_fevereiro - visitantes_janeiro

print(f"Total de visitantes únicos: {len(todos_visitantes)}")
print(f"Visitantes fiéis (3 meses): {visitantes_fieis}")
print(f"Novos visitantes em fevereiro: {novos_fevereiro}")
print(f"Quantidade de novos em fevereiro: {len(novos_fevereiro)}")
