resposta = 'SIM'
while resposta != 'NAO':
    valor = float(input('qual valor em dolar vc tem?: '))
    real = valor * 5.24
    doação = (real / 100 ) * 8
    print(f'voce tem R${real:.2f} reais')
    if real > 1000:
        print(f'voce tem mais de 1000 reais, e 8% deste valor {doação} vai ser para um hospital benificente')
    else:
        print('o valor não foi suficiente para doação')
    resposta = str(input('voce quer continuar? digite  SIM  ou NAO em maiúscula: '))  
print('finalizando...')    
