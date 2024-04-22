"""
Operadores lógicos
and (e) or (ou) not (não)
and - TOdas as condiçẽos presisam ser verdadeiras
Se qualquer valor considerado falsy, a 
expressão inteira será avaliada naquele valor 
São considerados falsos (que vc ja viu)
0 0.0 '' False
Também existe o tipo none que é 
usado para representar um não valor.
"""
#entrada = input('[E]ntrar [S]air: ')
#senha_digitada = input('Senha: ')
#senha_permitida = '1234'

#if entrada == 'E' and senha_digitada == senha_permitida:
#    print('Entrar')
#else:
#    print('Sair')

print(True and True and True)
print(True and False and True)
print(bool(0))
print(bool(0.0))
print(bool(''))