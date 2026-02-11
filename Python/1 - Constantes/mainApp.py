#Importa todas as constantes do arquivo constantes.py
import constantes

#Você pode importar constantes específicas
#from constantes import URL_API_USUARIO, TIMEOUT_SEGUNDOS

#Vamos usar as constantes do arquivo constantes.py

print("---------- Inicando a exibição dos dados das constantes ---------")
print(f"A área de um círculo é: {(8.00**2) * constantes.PI}")
print(f"URL base para a API principal é: {constantes.URL_API_USUARIO}")
print(f"Tempo limite de conexão: {constantes.TIMEOUT_SEGUNDOS} segundos")
print(f"As cores padrão são: {(constantes.CORES_PADRAO)}")
print(f"O debug está em modo: {constantes.MODO_DEBUG}")