"""
exercicio 
Exiba os indices da lista
0 Maria
1 Helena
2 Luiz
"""
lista = [ 'Maria','Helena','Luiz']
lista.append('Pedro')

tamanho = len(lista)

indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice])
