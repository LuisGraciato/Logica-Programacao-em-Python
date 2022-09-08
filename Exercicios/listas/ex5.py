valores = list()
cont = 0
while True:
    n = int(input('digite um numero'))
    valores.append(n)
    if n >= 0:
         cont += 1
    r = str(input('quer continuar? S/N'))
    if r in 'Nn':
        break
print(f' foram digitado {cont} numeros')
valores.sort(reverse=True)
print(f'a lista de valores em ordem decrescente é {valores}')
if 5 in valores:
    print(f'o valor 5 esta na lista, e esta na {valores.index(5)+1} posição ')
else:
    print('o valor 5 nao esta na lista')
