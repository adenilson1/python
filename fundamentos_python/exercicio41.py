varialvel_a = 1 or 0
varialvel_b = 0 or 1
print(varialvel_a, varialvel_b)
print(50 * '-')
nome = 'Maria Carmo'
if ' ' in nome:
    print(f'O nome {nome} tem espaços.')
else:
    print(f'O nome {nome} NÃO tem espaços.')

print(50 * '-')

numero = 10

if numero > 1:
    if numero > 2:
        if numero > 3:
            print('Numero maior que 3')
        else:
            print('Numero menor que 3')
    else:
        print('Numero menor que 2')
else:
    print('Numero menor que 1')