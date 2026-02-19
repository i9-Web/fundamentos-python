#============================================================
#Algoritmo que peça uma frase ao usuário e use o laço de 
# repetição for para contar quantas vogais (a, e, i, o, u
# – maiúscula ou minúscula) ela tem.
#============================================================
print("----------- Número de 1 até 100 (sem o dígito 3) -----------")
#Entrada de dados
frase = input("Digite uma frase: ")
contador = 0
vogais = "aeiouAEIOU"

#Processamento
for letra in frase:
    if letra in vogais:
        contador += 1
        
#Saída de dados
print(f"A frase tem {contador} vogais.")
