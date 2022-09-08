from random import randint
from time import sleep
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0,2)
print('suas opcoes:')
sleep(1)
print(' 0 PEDRA')
sleep(1)
print(' 1 PAPEL')
sleep(1)
print(' 2 TESOURA')
jogador = int(input('qual sua jogada?'))
sleep(1)
print('-'*10)
print('computador jogou {}'.format(itens[computador]))
sleep(1)
print('jogador jogou {}'.format(itens[jogador]))
print('-'*10)
print('JO')
sleep (1)
print('KEN')
sleep(1)
print('PO')
print('='*10)
if computador == 0: #pc jogou pedra
    if jogador == 0: #voce jogou pedra
        print('EMPATE')
    elif jogador == 1: #voce jogou papel
        print('Voce ganhou')
    elif jogador == 2: #voce jogou tesoura
        print('voce perdeu')
    else:
        print('jogada invalida')
elif computador == 1: #pc jogou papel
    if jogador == 0: #voce jogou pedra
        print('voce perdeu')
    elif jogador == 1: #voce jogou papel
        print('Empate')
    elif jogador == 2: #voce jogou tesoura
        print('voce ganhou')
    else:
        print('jogada invalida')    
elif computador == 2: #pc jogou tesoura
    if jogador == 0: #voce jogou pedra
        print('voce ganhou')
    elif jogador == 1: #voce jogou papel
        print('voce perdeu')    
    elif jogador == 2: #voce jogou tesoura
        print('empate')
    else:
        print('jogada invalida')    
print('='*10)        

