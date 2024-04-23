"""
Faça um programa que peça ao usuário para digitar um número
inteiro, informe se este número é par ou impar.
Caso o usuário não digite um 
número interio, inform que não é um número inteiro.
"""
numero_str = input('Digite um número inteiro: ')

try:
    numero_int = int(numero_str)

    if numero_int%2 == 0:
        print(f'{numero_int} é um número par')
    else:
        print(f'{numero_int} é um número impar')
except:
    print(f'{numero_str} não é um número inteiro')


