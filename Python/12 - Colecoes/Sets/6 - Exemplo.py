#Exemplos 6: Operações de interseção (intersection)
linguagens_joao = {"Python", "JavaScript", "Java", "C++"}

linguagens_maria = {"Python", "C#", "Java", "Go"}

# Interseção usando & ou intersection()
linguagens_comuns = linguagens_joao & linguagens_maria

linguagens_comuns2 = linguagens_joao.intersection(linguagens_maria)
print(f"Linguagens do João: {linguagens_joao}")
print(f"Linguagens da Maria: {linguagens_maria}")
print(f"Linguagens em comum usad &: {linguagens_comuns}")
print(f"Linguagens em comum usad intersection: {linguagens_comuns2}")

