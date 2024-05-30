"""extendendo uma lista com o uso de + ou do metodo extend"""

lista_a = [1,2,3]
lista_b = [4,5,6]

#uso do + 

lista_c = lista_a + lista_b
print(lista_c)

#uso do medoto extend
print(18*'-')

lista_a.extend(lista_b)
print(lista_a)