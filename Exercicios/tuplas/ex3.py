cont = 0
n = (int(input('digite um numero:')), int(input('mais um numero:')),
int(input('outro numero: ')), int(input('o ultimo numero: ')))
print(f'voce digitou os valores {n}')
print(f'o valor 9 apareceu {n.count(9)} vezes')   
if 3 in n:
    print(f'o valor 3 foi digitado na posição {n.index(3)+1}') 
else:
    print('o valor 3 n apareceu')  
print('os valores pares foram ', end='')
for numero in n:
    if numero % 2 == 0:
         print(numero, end='')
   
