
"""
Faça um programa que peça o primerio nome do usuário.
Se o nome tiver 4 letras ou menos esvreva "Seu nome é curto";
se tiver entre 5 e 6 letras, escreva "Seu nome é normal";
maior que 6 letras escreva "Seu nome é muito grande".

"""
primeiro_nome = input('Digite o seu nome: ')
tamanho_nome = len(primeiro_nome)

nome_curto = tamanho_nome >= 1 and tamanho_nome < 5 
nome_normal = tamanho_nome >= 5 and tamanho_nome < 7
nome_grande = tamanho_nome >= 7

if nome_curto:
    print(f'{primeiro_nome}, seu nome é curto')
elif nome_normal:
    print(f'{primeiro_nome}, seu nome é normal')
elif nome_grande:
    print(f'{primeiro_nome}, seu nome é grande')
else:
    print('Digite pelo menos uma letra')

