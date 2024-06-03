"""
INtrodução ao empacotamento e desempacotamento
+ tuples(tuplas)
"""
#nomes = ['M','H','L']
#print(nomes)

#n1,n2,n3 = ['M','H','L']
#print(n3)

#criando uma variavel resto com _

n1,*_ = ['M','H','L']
print(n1,*_)

print(25*'-')

_,n2,*_ = ['M','H','L']
print(n2)

print(25*'-')

_,_,n3 = ['M','H','L']
print(n3)

