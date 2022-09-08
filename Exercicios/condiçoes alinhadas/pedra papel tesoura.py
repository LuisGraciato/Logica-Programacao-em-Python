from random import choice
print('vamos jogar jokenpo')
vc = str(input('escolha algo'))
print('agora é minha vez')
lista = ['pedra','papel','tesoura']
pc = choice(lista)
print('o computador escolheu {}'.format(pc))
if vc == 'pedra' and pc == 'papel':
    print('VOCE PERDEU')
elif vc == 'pedra' and pc == 'tesoura':
    print('VOCE GANHOU') 
elif pc == 'pedra' and vc == 'papel':
    print('VOCE GANHOU')
elif pc == 'pedra' and vc == 'tesoura':
    print('VOCE PERDEU')
else:
    print('EMPATE')    