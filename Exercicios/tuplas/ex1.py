cont = ('zero', 'um', 'dois', 'trres','quatro','cinco','seis','sete','oito',' nove','dez')
while True:
    n = int(input('digite um numero'))
    if 0 <= n <= 20:
        break
    print('tente novamente', end = '')
print(f'voce digitou o numero {cont[n]}')
