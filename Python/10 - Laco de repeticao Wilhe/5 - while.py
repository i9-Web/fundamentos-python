#Exemplo de Loop infinito controlado com break: 
# while True cria um loop infinito, mas o break 
# interrompe assim que o usuário digita “sair”
#Entrada de dados

while True:
    nome = input("Digite seu nome (ou 'Sair' para encerrar): ")
    if nome.upper() == "SAIR":
        break
    
    print(f"Olá, {nome}!")



    