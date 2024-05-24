"""COMO FUNCIONA O LAÇO FOR
iteravel -> str, range, etc (__iter__)
iterator -> quem sabe entregar um valor por vez
next -> entrega o próximo valor
iter -> entrega seu iterador
"""

texto = 'Adenilson'
iterador = iter(texto)

#esse codigo exlica o real funcionamento do laço for
"""
while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break
"""
#logo todo o codigo acima é a explicação do simples codigo do laço for abaixo

for letra in texto:
    print(letra)