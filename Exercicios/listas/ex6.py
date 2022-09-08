temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('nome  ')))
    temp.append(float(input('peso  ')))
    if len (princ) == 0:
        mai = men = temp[1]
    else:
        if temp [1] > mai:
            mai = temp[1]
        if temp [1] < men:
            men = temp[1]

    princ.append(temp[:])
    temp.clear()

    resp = str(input('quer continuar S/n'))
    if resp in 'Nn':
        break
print(f'ao todo cadastraram {len(princ)}')
print(f'o maior peso foi de {mai} kg e o menor foi de {men} Kg')
for p in princ:
    if p[1] == mai:
        print(f'{p[0]}')