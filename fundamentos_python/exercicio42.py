nome = input(  'Digite o seu nome: ')
idade = input('Digite a sua idade: ')
nome_invertido = nome

print(30*'-')

if nome == '' or idade == '':
    print('Desculpe, você deixou espaços vazios')
else:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome_invertido[::-1]}')

    if ' ' in nome:
        print('Seu nome tem espaços')
    else:
        print('Seu nome nao tem espaços')

    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[len(nome)-1]}')

