preco = float(input('quanto vc vai pagar neste produto?'))
dinheiro = (preco/100)*90
cartao = (preco/100)*95
x2 = preco 
x3 = (preco/100)*120
tipo = str(input('qual a forma de pagamento? dinheiro\ncartao,\n2x no cartao \nou 3x no cartao \n RESPONDA AQUI'))
if tipo == dinheiro:
    print('o valor deu {}'.format(dinheiro))
elif tipo == cartao:
    print('o valor deu {}'.format(cartao))  
elif tipo == x2:
    print('o valor deu {}'.format(x2))
else:
    print('o valor deu {}'.format (x3))

