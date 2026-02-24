#============================================================
#Algoritmo que simule o jogo de adivinhação. O algoritmo deve
# importar o módulo “random”, selecionar um número aleatório e
# usuário deve dar um palpites de que número foi sorteado até
# acertar. Dá dicas se está alto ou baixo.
#============================================================
import random
print("----------- Jogo da adivinhação -----------")
print("tente adivinhar o número que eu pensei (de 1 até 100!)\n")

#Entrada de dados
numero_secreto = random.randint(1, 100)
tentativas = 0

while True:
    palpite = int(input("Digite um palpite: "))
    tentativas += 1

    if palpite < numero_secreto:
        if palpite < numero_secreto - 5:
            print("Está frio! Tente um número maior.")
        else:
            print("Está quente! Tente um número maior.")

    elif palpite > numero_secreto:
        if palpite < numero_secreto + 5:
            print("Está frio! Tente um número menor.")
        else:
            print("Está quente! Tente um número menor.")
    else:
        print(f"Parabéns! Você acertou em {tentativas}.")
        print(f"O número secreto era: {numero_secreto}")
        break
