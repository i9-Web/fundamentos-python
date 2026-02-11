#Declaração de constantes
#Exemplo de constante com o tipo de dado int (inteiros) 
TIMEOUT_SEGUNDOS = 27
#Exemplo de constante com o tipo de dado float (número real) 
PI = 3.14159
#Exemplo de constante com o tipo de dado string (cadeia de caracteres) 
URL_API_USUARIO = "https://api.exemplo.com/v1/usuarios"
#Exemplo de constante com o tipo de dado bool (booleano - Verdadeiro ou Falso) 
MODO_DEBUG = True
#xemplo de constante com o tipo de dado tupla (coleção imutável - array imutável) 
CORES_PADRAO = ("azul", "branco", "verde", "amarelo")

#Saída de dados 
print("---------- Inicando a exibição dos dados das constantes ---------")
print(f"A área de um círculo é: {(8.00**2) * PI}")
print(f"URL base para a API principal é: {URL_API_USUARIO}")
print(f"Tempo limite de conexão: {TIMEOUT_SEGUNDOS} segundos")
print(f"As cores padrão são: {(CORES_PADRAO)}")
print(f"O debug está em modo: {MODO_DEBUG}")