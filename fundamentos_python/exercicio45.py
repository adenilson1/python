
"""
Faça um programa que peça o primerio nome do usuário.
Se o nome tiver 4 letras ou menos esvreva "Seu nome é curto";
se tiver entre 5 e 6 letras, escreva "Seu nome é normal";
maior que 6 letras escreva "Seu nome é muito grande".

"""
primeiro_nome = input('Digite o seu nome: ')
numero_letras_do_nome = len(primeiro_nome)

nome_curto = numero_letras_do_nome < 5 
nome_normal = numero_letras_do_nome >= 5 and numero_letras_do_nome < 7


if nome_curto:
    print(f'{primeiro_nome}, seu nome é curto')
elif nome_normal:
    print(f'{primeiro_nome}, seu nome é normal')
else:
    print(f'{primeiro_nome}, seu nome é grande')


print(numero_letras_do_nome)
