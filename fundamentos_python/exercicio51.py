import os

palavra_secreta = 'carro'
letra_certa = ''
tentativas = 0


while True:
    
    letra = input('Digite uma letra: ')
    if len(letra) != 1:
        print('Digite apenas uma letra')
        continue

    if letra in palavra_secreta:
        letra_certa += letra
    palavra_certa =''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letra_certa:
           palavra_certa += letra_secreta
        else:
            palavra_certa += '*'
        
    tentativas +=1
    print(f'Palavra formada: {palavra_certa}')
    if palavra_certa == palavra_secreta:
        os.system('clear') # limpar terminal
        print(f'PARABÉNS!!!, VOCÊ ACERTOU PALAVRA SECRETA: {palavra_secreta}')
        print(f'Você usou {tentativas} tentativas')
        #para zera o programa
        letra_certa = ''
        tentativas = 0      

    
