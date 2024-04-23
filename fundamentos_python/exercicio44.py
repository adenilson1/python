"""
Fça um programa que pergunte a hora ao usuário e,
baseando-se no horário descrito, exibe a saudação
apropriada. Ex. Bom dia 0-11, Boa tarde 12-17 
e Boa noite 18-23
"""

pergunta = input('Que horas são ?: ')
resposta = float(pergunta)

DIA = 0
TARDE = 12
NOITE = 18

bom_dia = resposta >= DIA and resposta < TARDE
boa_tarde = resposta>= TARDE and resposta < NOITE
boa_noite = resposta>= NOITE 

if bom_dia:
    print(f'Bom dia são {resposta:.2f} horas')
elif boa_tarde:
    print(f'Boa tarde são {resposta:.2f} horas')
else:
    print(f'Boa noite são {resposta:.2f} horas')