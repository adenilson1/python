"""
Cuidados com tipos de dados mutáveis - list e copy
= - copiar o valor (imutável)
= - apontar para o mesmo valor na memória(mutável)
"""

nome = 'carro'
noutro_valor = nome
nome = 'avião'
print(nome)
print(noutro_valor)

print(30*'-')

lista_a = ['carro', 'avião', 'maria',1,True,1.2]
lista_b = lista_a
lista_c = lista_a.copy()
lista_a[0]= 'qualquer coisa'

print(lista_b)
print(lista_c)