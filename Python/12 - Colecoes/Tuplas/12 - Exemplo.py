#Exemplos 12: Tupla nomeada (NamedTuple) pytho
from collections import namedtuple

#Criando uma tupla nomeada
Pessoa = namedtuple('Pessoa', ['nome', 'idade', 'cidade'])

francisco = Pessoa('Francisco', 56, 'Aracaju')
print(f"Nome: {francisco.nome}")
print(f"Idade: {francisco.idade}")
print(f"Cidade: {francisco.cidade}")
print(f"Tupla completa: {francisco}")