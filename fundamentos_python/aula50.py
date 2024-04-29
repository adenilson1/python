"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imútaveis que vimos: str, int, float, bool
"""
string = 'luiz Otávio'
outra_varialvel = f'{string[:3]}ABC{string[4:]}'
#string[3] = 'ABC'
##print(outra_varialvel)
print(string.zfill(100))