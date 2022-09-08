ano = int(input('diga o ano q vc nasceu'))
if (2022 - ano) == 18:
    print('é hora de se alistar')
elif (2022 - ano) < 18:
    print('ainda vai se alistar')
else:    
    print('ja passou o tempo, {} ano(s) que vc deveria ter se alistado'.format())   