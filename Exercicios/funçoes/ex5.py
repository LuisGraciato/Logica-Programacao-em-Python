c = ('\033[m',
    '\033[0;30;41m'
)

def ajuda(com):
    help(com)
    print(c[0],end='')

def título(msg,cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('-'*tam)
    print(  {msg})
    print('-'*tam)
    print(c[0],end='')

comando = ''
while True:
    título('SISTEMA DE AJUDA PyHELP',1)
    comando = str(input("funçao ou biblioteca: "))
    if comando.upper()=='FIM':
        break
    else:
        ajuda(comando)
título('ATE LOGO',1)