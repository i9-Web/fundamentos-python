#============================================================
#Algoritmo que peça o usuário e a senha até que seja acertados
# os dois ao mesmo tempo. Exemplo de Usuário: admin e de 
# Senha: 1234.
#============================================================
print("----------- Sistema de login -----------")
#Entrada de dados
USUARIO_CORRETO = "admin"
SENHA_SECRETA = "1234"

while True:
    usuario = input("Informe o usuário: ")
    senha = input("Informe a senha: ")

    if usuario == USUARIO_CORRETO and senha == SENHA_SECRETA:
        print(f"Login bem-sucedido! \n Seja bem-vindo {usuario} ao sistema")
        break
    else:
        print(f"Usuário e/ou senha incorreta, \n Tente novamente.")
