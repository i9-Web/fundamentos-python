#Exemplo 1: Recebenddo unoa string do usuário
nome_usuario = input("Qual é o seu nome? ")
print(f"Prazer em conhecê-lo(a), {nome_usuario}!")
#Exemplo 2:Recebe uma string e convertendo para um número inteiro
idade_str = input("Quantos anos você tem?") 
idade_int = int(idade_str) #Converte a string (texto) em um número inteiro
#Exemplo 3: Recebe uma string e convertendo para um número fracionário (int)
altura_str = input("Qual é a sua altura em metros (Ex: 1.75)?")
altura_float = float(altura_str) #Converte a string (texto) em um número fracionário (float)

print(f"Confira as informações Sr(a) {nome_usuario}")
print(f"Sua idade é: {idade_int} ano.")
print(f"Sua altura é {altura_float:.2f} metros.")
