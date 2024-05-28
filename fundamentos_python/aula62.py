"""
Lista em Python
Tipo list - mutável
SUporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - indices e fatiamento
Médotos úteis: uppend, insert, pop, del, clear, extend, +
"""

string = 'ABCDE'
#lista = []
#print(lista, type(lista))
#print(bool(lista))

#          0    1      2       3    4
lista = [ 123, True, 'Pedro', 1.2, []]
#          -5   -4     -3      -2   -1

print(lista)
print(lista[2], type(lista[2]))
print(lista[2].upper(), type(lista[2]))

print(lista[2] == lista[-3]) # true

lista[-3] = 'Maria'
print(lista)