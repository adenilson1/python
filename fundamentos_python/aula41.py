"""
Operadores lógicos
and (e) or (ou) not (não)
or -> Qualque condição verdadeira avalia
toda a expressão como verdadeira.
Se qualquer valro for considerado verdadeiro,
a expressão interia será avaliada naquele valor.
São considerados falsy (que vc já viu)
 0 0.0 '' False
 Também existe o tipo none é usado para representar um não valor
"""

#entrada = input('[E]ntrar [S]air: ')
#senha_digitada = input('Senha: ')
#senha_permitida = '1234'

#if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
#    print('Entrar')
#else:
#    print('Sair')

senha = input('Senha: ') or 'Sem senha'
print(senha)
