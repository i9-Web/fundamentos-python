#Em uma equeção os parenteses mais internos são eliminados 
# primeiro e depois se segue a ordem de execução sequecial
x = 2
y = 3
z = 4
resultado_potencia = x ** y
print(f"Potência {x} elevado a {y} é igual a: {resultado_potencia} ")

expressao1 = x + y * z / x
expressao2 = (x + y) * z / x
expressao3 = x + (y * z ) / x
expressao4 = (x + y) * (z / x)
print(f"---------- Resultado da expressões aritméticas ----------")
print(f"Expressão 1: x + y * z / x = {x} + {y} * {z} / {x} = {expressao1}")
input("Proximo")
print(f"Expressão 2: (x + y) * z / x = ({x} + {y}) * {z} / {x} = {expressao2}")
input("Proximo")
print(f"Expressão 3: x + (y * z ) / x = {x} + ({y} * {z}) / {x} {expressao3}")
input("Proximo")
print(f"Expressão 4: (x + y) * (z / x) = ({x} + {y}) * ({z} / {x}) = {expressao4}")

