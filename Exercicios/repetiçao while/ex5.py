n = int(input('digite um numero: '))
c = n
f = 1
for n in range(n,1):
    print(c)
    print(' x ' if c > 1 else '=')
    f*= c
    c-= 1
    print(f'{f}')
