n = cont = soma = 0
while True:
    n = int(input('digite um valor 999 para parar'))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'voce digitou {cont} numeros e a soma entre eles foi {soma}')