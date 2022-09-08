vel = float(input(' a quantos km vc está?'))
multa = (80 - vel) * -7
if vel <= 80:
     print('voce esta na velociade correta')
else:
    
    print('voce esta acima da velocidade e foi multado em R${}0'.format(multa))  
      