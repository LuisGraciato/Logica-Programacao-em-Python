s = 0
mulheres_menos_20_anos = 0
for c in range (1,3):
    nome = str(input('seu nome: '))
    idade = int(input('sua idade: '))
    sexo = str(input('seu sexo, (M) ou (F)')).upper()
    s = (s + idade) 
    if sexo == "F" and idade < 20:
        mulheres_menos_20_anos += 1
print(f' a média da idade do grupo é de {s/2} anos') 
print(f' existem {mulheres_menos_20_anos} mulheres com menos de 20 anos')
