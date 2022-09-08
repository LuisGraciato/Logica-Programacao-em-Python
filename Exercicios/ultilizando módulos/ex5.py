from random import choice
p = str(input('primeiro aluno'))
s = str(input('segundo aluno'))
t = str(input('terceiro aluno'))
q = str(input('quarto aluno'))
lista = [p,s,t,q]
escolhido = choice(lista)
print('o escolhido foi {}'.format(escolhido)) 