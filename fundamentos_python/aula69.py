"""
tipo tupla -> é uma lista imutaável
a tupla é pouvco mais eficiente que a lista
e nao se coloca colchetes na tupla
"""

nomes = ('M','H','L') # TUPLA
print(nomes)

# a tupla nao aceita os metodos da lista, pq como foi dito ela é imutável

#converte tupla em lista e vice versa

nomes = list(nomes)
print(nomes)

nomes = tuple(nomes)
print(nomes)