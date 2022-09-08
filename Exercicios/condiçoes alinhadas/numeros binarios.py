n = int(input('digite um numeiro'))
print('''escolha uma das bases para conversão'
(1) BINARIO
(2) OCTAL
(3) HEXADECIMAL''')
opcao = int(input('sua opção:'))
if opcao ==1:
    print('{} convertido bara BINARIO é {}'.format (n, bin(n)))

