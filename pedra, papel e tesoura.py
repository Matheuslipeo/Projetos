from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
pc = randint(0, 2)
print('='*20)
print('''PEDRA, PAPEL E TESOURA
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')
print('='*20)
jogador = int(input('Qual a sua jogada? '))
print('-'*20)
print('O computador jogou {}'.format(itens[pc]))
print('Você jogou {}'.format(itens[jogador]))
print('-'*20)
sleep(1)
if pc == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('VOCÊ VENCEU')
    elif jogador == 2:
        print('O COMPUTADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA')
if pc == 1:
    if jogador == 0:
        print('O COMPUTADOR VENCEU')
    elif jogador ==1:
        print('EMPATE')
    elif jogador ==2:
        print('VOCÊ VENCEU')
    else:
        print('JOGADA INVÁLIDA')
if pc == 2:
    if jogador ==0:
        print('VOCÊ VENCEU')
    elif jogador ==1:
        print('O COMPUTADOR VENCEU')
    elif jogador ==2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')
