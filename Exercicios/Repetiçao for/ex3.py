s = 0
cont = 0
for c in range(1,451,2):
    if c % 3 == 0:
        cont = cont + 1
        s = s + c
print(' a soma d todos os {} valores é {}'.format (cont, s))
     