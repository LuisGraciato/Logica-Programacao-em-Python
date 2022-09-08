n1 = int(input('digte um valor : '))
n2 = int(input('agora outro: '))
opcoes = str(input('voce quer, 1 somar, 2 multplicar, 3 maior, 4 novos numeros ou 5 sair: '))
while opcoes != '5':
  if opcoes == '1':
    print(n1 + n2)
    opcoes = str(input('voce quer, 1 somar, 2 multplicar, 3 maior, 4 novos numeros ou 5 sair: '))
  elif opcoes == '2':
    print(n1*n2)
    opcoes = str(input('voce quer, 1 somar, 2 multplicar, 3 maior, 4 novos numeros ou 5 sair: '))
  elif opcoes == '3':
     maior = n1
     if n2 > maior:
      maior = n2
     print(f' o  maior é {maior}')
     opcoes = str(input('voce quer, 1 somar, 2 multplicar, 3 maior, 4 novos numeros ou 5 sair: '))
  else: 
      print('invalido') 
      opcoes = str(input('voce quer, 1 somar, 2 multplicar, 3 maior, 4 novos numeros ou 5 sair: '))
print('saindo....')        
