"""
Repetiçoes 
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Looop infinito -> Quando um codigo não tem fim
"""
contador = 0
while contador <= 20:

    contador += 1

    if contador == 3:
        print('Não vou mostrar', contador)
        continue

    if contador >= 7 and contador <= 10:
        print('Não mostrar', contador)
        continue

    print(contador)

    if contador == 15:
        break
  

print('acabou')