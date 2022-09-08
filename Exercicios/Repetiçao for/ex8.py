totmaior = 0
totmenor = 0
for c in range (1,4):
    ano = int(input(f' ano de nascimento da {c} pessoa: '))
    idade = 2022 - ano
    if idade <= 17:
        totmenor = totmenor + 1
    else:
        totmaior = totmaior + 1
print(f'ao todos temos {totmenor} pessoas menor de idade e {totmaior} maiores de idade')
        