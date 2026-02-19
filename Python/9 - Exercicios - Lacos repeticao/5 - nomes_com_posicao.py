#============================================================
#Algoritmo que dada a lista nomes = ["Ana", "Bia", "Carlos", 
# "Diego"], imprima os nomes da lista com sua posição, 
# começando do 1 (ex: 1 - Ana)
#============================================================
print("----------- Lista de nomes com posição -----------")
nomes = ["Ana", "Bia", "Carlos", "Diego"]

for i in range(len(nomes)):
    print (f"{i + 1} - {nomes[i]}") 