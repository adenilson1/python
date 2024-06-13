"""
Fazer uma lista de compra com listas.
O usúuário deve ter a possibilidade de inserir, apagar e listar
os valores da sua lista. Não permitir que o programa quebre 
com erros de índices inexistentes na lista
"""

import os

lista_compras = []

while True:
    print('Escolha uma opção: ')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('clear')
        item = input('Digite o item a sua lista de compra: ')
        lista_compras.append(item)
    elif opcao == 'a':
        indice_str = input('Escolha o índice do item que deseja apagar: ')

        try:
            indice_int = int(indice_str)
            del lista_compras[indice_int]
        except:
            print('Índice esolhido não encontrado no lista')
    
    elif opcao == 'l':
        os.system('clear')

        if len(lista_compras) == 0:
            print('Lista de compras vazia')
        for i, item in enumerate(lista_compras):
            print(i,item)
    else:
        os.system('clear')
        print('Escolha uma opção válida')

