import random
cont = 0
print('vou pensar em um numero de 0 a 10')
n = random.randint(0,10)
jogador = int(input('tente adivinhar que numero pensei :  '))
while jogador != n:
    jogador = int(input('tente novamente: '))
    cont += 1
print(f'Voce acertou!, e precisou de {cont} Tentativas')    
