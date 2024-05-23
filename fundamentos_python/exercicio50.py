"""JOGO DA ADIVINHAÇÃO"""
"""ACERTE O NUMERO"""
numero_secreto = 42
numero_de_tentivas = 3

while numero_de_tentivas > 0:
    chute = int(input('Digite um número: '))
    print(f'Você digitou o número {chute}')

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print('Você acertou o número secreto !!!')
        break
    elif maior:
        print('Seu número é maior que o número secreto')
    elif menor:
        print('Seu número é menor que o número secreto')
    else:
        print('Digite um número inteiro')
    
    numero_de_tentivas -=1
    print(f'Você tem {numero_de_tentivas} tentivas')
print('****FIM DE JOGO****')