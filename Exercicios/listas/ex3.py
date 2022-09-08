numeros = list()
while True:
    n = int(input('digite um valor'))
    if n not in numeros:
        numeros.append(n)
        print('valor adicoinado')
    else:
        print('valor duplicado')    
    resp = (str(input('quer continuar? S/N')))
    if resp in 'Nn':
        break    
numeros.sort()
print(f'voce digitou os valores {numeros}')