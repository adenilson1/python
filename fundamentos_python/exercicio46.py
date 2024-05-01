"""
Iterando strings com while
"""
       #012345678
nome = 'Brasil' # iteraveis
tamanho_nome = len(nome)
novo_nome = ''
indice = 0

while indice < tamanho_nome:
      novo_nome += f'*{nome[indice]}'
      indice += 1
print(f'{novo_nome}*')


#nova_string += '*A*d*e*n*i*l*s*o*n'