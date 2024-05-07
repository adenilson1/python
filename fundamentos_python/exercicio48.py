#Outra calculadora

while True:

    numero_1 = input('Digite um numero: ')
    numero_2 = input('Digite outro numero: ')
    operador = input('Digite um operador: +-*/: ')
    numeros_validos = None

    print(25 * '-')

    try:
        n_1 = float(numero_1)
        n_2 = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None
    if numeros_validos is None:
        print('Um ou ambos os números são inválidos')
        continue

    operador_valido = '+-*/'
    if operador not in operador_valido:
        print('Operador inválido')
        continue

    match operador:
        case '+':
            resultado = n_1 + n_2
        case '-':
            resultado = n_1 - n_2
        case '*':
            resultado = n_1 * n_2
        case '/':
            if n_2 != 0:
                resultado = n_1 / n_2
            else:
                print('Divisão por zero, operação inválida')
                continue
       
    
    print(f'O rasultado de {n_1} {operador} {n_2} é {resultado}')


    sair = input('Digite [s]im para sair: ').lower().startswith('s')
    if sair is True:
        break


