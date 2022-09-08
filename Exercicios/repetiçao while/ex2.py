sexo = str(input('qual seu sexo? (M) ou (f)')).upper()
while sexo not in 'MF':
    sexo = str(input('dados invalidos, digite novamente ')).upper()
print(f'sexo {sexo} registrado com sucesso')    