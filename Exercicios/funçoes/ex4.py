def voto(ano):
    atual = 2022
    idade = atual - ano
    if idade < 16:
        return f'com {idade} anos: nao vota'
    elif 16<= idade < 18 or idade > 65:
        return f'com {idade} o voto é opcional'
    else:
        return f'com {idade} o voto é obrigatorio'  


print(voto(2006))
    