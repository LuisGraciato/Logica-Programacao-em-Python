print('LOJA DO LUISAO')
resp = 'S'
totdin = totalcima = menor = cont =  0
barato = ''
while resp in 'Ss':
    produto = str(input('nome do produto'))
    preço = int(input('qual o preço: R$ '))
    resp = str(input('quer continuar?'))
    totdin += preço
    cont += 1
    if preço >= 1000:
        totalcima += 1 
    if cont == 1:
        menor = preço
        barato = produto
    else:
        if preço < menor:
            menor = preço
            barato = produto
print(f'o total da compra foi {totdin}')
print(f'temos {totalcima} produtos custando mais de 1k')
print(f'o produto mais barato custa {menor}')