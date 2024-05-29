"""
Lista em Pytho
Tipo list - mutável
Suporta vários valores de qualquer tipo
Conhecimento reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, + 
cread read update delete
criar,ler,alterar,apagar = list[i] (CRUD)
"""

lista = [10, 20, 30, 40] #lista de inteiros - > criar lista
#print(lista) -> le lista
#lista[2] = 300 -> alterar a lista
#print(lista)
#del lista[2] -> deletar lista
#print(lista)

#adicionando elementos no final da lista
lista.append(50)
lista.append(60)
lista.append(70)
#print(lista)

#remover elementos do final da lista
lista.pop()
print(lista)