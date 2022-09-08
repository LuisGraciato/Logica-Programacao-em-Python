n = [ [], []]
valor = 0
for c in range(1,8):
    valor = int(input('digite um valor  '))
    if valor %2 == 0:
        n[0].append(valor)
    else:
        n[1].append(valor)
n[0].sort()
n[1].sort()
print(f' os valores pares são : {n[0]} e os impares {n[1]}')