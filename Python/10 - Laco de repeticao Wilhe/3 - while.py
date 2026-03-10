#Exemplo da repetição de um input:
# Repete o teste de input enquanto nãoacertar o palpite
#Entrada de dados
palavra = "Python"
palpite = ""
contador = 0

while palpite != palavra:
    palpite = input("Digite uma palavra: ")
    contador += 1
    
print("Parabén, você acertou a palavra na ", contador, 
      "º tentativa!")
