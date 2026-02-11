comando = ["ligar", "sala"]

match comando:
    case ["ligar", local]:
        print(f"Ligando a luz da {local}.")
    case ["desligar", local]:
        print(f"Desligando a luz da {local}.")
    case ["tocar", musica]:
        print(f"Tocando a música: {musica}.")
    case _:
        print("Comando não reconhecido.")
