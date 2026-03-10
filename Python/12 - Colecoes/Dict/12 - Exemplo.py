#Exemplos 12:  Dicionário aninhado (JSON-like)
empresa = {
    "nome": "Xpto Ltda",
    "funcionarios": [
        {"id": 1, "nome": "João", "salario": 5000},
        {"id": 2, "nome": "Maria", "salario": 6500},
        {"id": 3, "nome": "Pedro", "salario": 4800}
    ],
    "ativo": True
}

print("Salário do funcionário 2:", empresa["funcionarios"][1]["salario"])






