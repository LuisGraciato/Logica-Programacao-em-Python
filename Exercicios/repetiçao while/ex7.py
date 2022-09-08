resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    n = int(input('digite um numero'))
    soma += n
    quant += 1
    media = soma / quant
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n        
    resp = str(input('quer continuar s ou n ')).upper()
print(f'vc digitou {quant} numeros e media foi {media:.2f}')  
print(f'o maior valor foi {maior} e o menor foi {menor}')  