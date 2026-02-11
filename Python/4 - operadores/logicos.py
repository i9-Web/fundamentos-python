#Operadores lógico
#Usados para comprar expressões lógica booleanas
# and Retorna true (Verdadeiro) se todas as entradas forem verdadeiras
# or  Retorna true (Verdadeiro) se pelo menos uma das estradas for verdadeiras
# not Inverte o valor booleano de entrada

#Exemplo 1: Usando o operador and
idade = 25
tem_habilitacao = True
pode_dirigir = (idade >= 18) and tem_habilitacao
print(f"Essa pessoa pode dirigir? : {pode_dirigir}")

#Exemplo 2: Usando o operador or
tem_passaporte = False
tem_visto = True
pode_viajar = tem_passaporte or tem_visto
print(f"Essa pessoa pode viajar? {pode_viajar}")

#Exemplo 3: Usando o operador not
esta_chovendo = True
tenho_guarda_chuva = False
posso_sair = esta_chovendo or  tenho_guarda_chuva
posso_sair_negado = not posso_sair

print(f"Posso sair? : {posso_sair}")
print(f"Posso sair? : {posso_sair_negado}")