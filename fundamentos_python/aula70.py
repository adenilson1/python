"""
Enumerate para enumerar valores iteráveis (pega indice)
"""

lista = [ 'M','H','L']
lista.append('J')

# 1) forma
lista_enumerada = enumerate(lista)
print(lista_enumerada) # endereco de memoria
print(next(lista_enumerada)) # posicao de indice, valor)
print(25*'-')

# 2) forma: exibição de todos os indices e valores da lista
for item in lista_enumerada:
    print(item)
print(25*'-')

# 3) forma: uso direto do enumerate no laço for
for item in enumerate(lista):
    indice, valor = item
    print(indice, valor)
print(25*'-')

# 4) forma: imprimindo direto do indice e do valor no laço for
for indice, valor in enumerate(lista):
    print(indice, valor)
print(25*'-')

# 5) forma: usando a lista como uma tupla
for tupla_enumerada in enumerate(lista):
    print('For da tupla:')
    for valor in tupla_enumerada:
        print(f'\t{valor}')
