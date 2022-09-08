import time
n1 = float(input('ola, digite o peso da primeira pessoa'))
print('recebido..')
time.sleep(2)
n2 = float(input('beleza, agora o da segunda pessoa'))
print('recebido...')
time.sleep(2)
m = (n1+n2)/2
print ('calculando...')
time.sleep(3)
print('bom a media entre as duas pessoas é de {} kg'.format(m))