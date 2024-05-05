"""Calculadora com while"""


#primeiro_numero = input('Digite o primeiro numero: ')
#segundo_numero = input('Digite o segundo numero: ')
#operador = input('Digite a operação "+", "-", "*", "/": ')

while True:
        primeiro = input('Digite o primeiro valor: ')
        segundo = input('Digite o segundo valor: ')
        operador = input('Escolha o operador: +, -, *, /: ')
        resultado = 0
        print(25*'-')
        if operador == '+':
                resultado = float(primeiro) + float(segundo)
        elif operador == '-':
                resultado = float(primeiro) - float(segundo)
        elif operador == '*':
                resultado = float(primeiro) * float(segundo)
        elif operador == '/':
                resultado = float(primeiro) / float(segundo)
        else:
                print('Digite uma operação valida')
        print(f'O resultado da operação {primeiro} {operador} {segundo} = {resultado:.2f}')

        print(25*'-')

        sair = input('Digite [s]im para sair: ').lower().startswith('s')

        if sair is True:
                break
        
        print(25*'-')

