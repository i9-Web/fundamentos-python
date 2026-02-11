#Operadores de comparação ou operador de relacionamento
#São usados para comparara dois valores, resultando em um valor lógico booleano (Tr ou False)
#Operadores
# ==    Operador de igualdade       5 == 5      True
# !=    Diferente de                5 != 10     True
# >     Maior que                   10 > 5      True
# <     Menor que                   5 < 10      True
# >=    Maior ou igual a            10 >= 10    True
# <=    Menor ou igual a            10 <= 10    True

#Exemplo 1: Comparação de iguadade e diferença 
a = 10
b = 10
c = 20

print(f"a == b: {a == b }")
print(f"a != c: {a != c }")

#Exemplo 2: Comparação de maior/menor
idade_minima = 18
idade_usuario = 20

print(f"Usuário é maior de idade? {idade_usuario >= idade_minima}")

#Exemplo 3: Comparação de Strings
texto1 = "Python"
texto2 = "python"

print(f"texto1 igual ao texto2? : {texto1} == {texto2} : {texto1 == texto2}")

#Exemplo 3a: Função .lower()
texto1 = "Python"
texto2 = "python"

print(f"texto1 igual ao texto2? : {texto1.lower()} == {texto2.lower()} : {texto1.lower() == texto2.lower()}")

#Exemplo 3b: Função .upper
texto1 = "Python"
texto2 = "python"

print(f"texto1 igual ao texto2? : {texto1.upper()} == {texto2.upper()} : {texto1.upper() == texto2.upper()}")