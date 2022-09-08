pt = int(input('digite o primeiro termo'))
razao = int(input('agora a razão '))
termo = pt
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} ->', end= '')
        termo += razao
        cont += 1
    print('pausa')
    mais = int(input('quantos termos vc quer mostrar a mais?'))
print('fim')