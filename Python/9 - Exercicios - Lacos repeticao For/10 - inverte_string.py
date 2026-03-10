#============================================================
#Algoritmo que que dado o texto = "Fundamentos de Python", use
#  for para montar e imprimir a string invertida (“nohtyP ed
#  sotnemadnuF”).
#============================================================
print("----------- Inverte as sequência de letras de uma string -----------")
#Entrada de dados
texto = "Fundamentos de Python"
texto_invertido = ""

for letra in texto:
    texto_invertido = letra + texto_invertido

print("Texto original: ", texto)
print("Texto invertido: ", texto_invertido)