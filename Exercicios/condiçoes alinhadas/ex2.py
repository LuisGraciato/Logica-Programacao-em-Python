valorcasa = float(input('digite o valor da casa'))
salario = float(input('agr o salario'))
anos = float(input('em quantos anos vai pagar?'))
prestacao = (valorcasa/anos)/12
if prestacao > (salario/100) *30:
    print('voce nao pode realizar o emprestimo')
else:
    print('o valor da prestação é de R${:.2f} mensais , durante {} anos'.format(prestacao, anos))    
