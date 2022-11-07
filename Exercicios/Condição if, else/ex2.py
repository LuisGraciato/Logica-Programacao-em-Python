import random
import time
print ('estou pensando em um numero..')
print ('se voce adivinhar de 1 a 5 eu te dou parabens')
pc = random.randint(1,5)
voce = int(input('digite um numero de 1 a 5'))
print('ESTOU PENSANDO...')
time.sleep(5)
if voce == pc:
    print('VOCE ACERTOU ')
else:
    print('vc errou')


