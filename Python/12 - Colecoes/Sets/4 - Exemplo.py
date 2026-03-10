#Exemplos 4: Removendo elementos do set
animais = {"gato", "cachorro", "pássaro", "peixe"}
print(f"Conjuto de animal: {animais}")
input("Pressione enter!")
# remove() - gera erro se não existir
animais.remove("peixe")
print(f"Conjuto de animal: {animais}")
input("Pressione enter!")
# discard() - não gera erro se não existir
animais.discard("hamster") 
input("Pressione enter!")
# pop() - remove um elemento aleatório
removido = animais.pop()
print(f"Animais restantes: {animais}")
print(f"Animal removido aleatoriamente: {removido}")


