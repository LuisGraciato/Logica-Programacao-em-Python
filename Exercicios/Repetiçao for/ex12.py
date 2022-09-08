from time import sleep
for c in range(0,1):
 sexo= str(input('qual seu sexo? (M) ou (F): ')).upper()
 idade = int(input('sua idade: '))
 resposta = str(input('vc gostou do produto? (sim) ou (não): ')).upper()
sleep(1)
print('1) QUANTAS PESSOAS FORAM ENTREVISTADAS?')
sleep(1)
if sexo == 'M':
    print('foi entrevistado apenas um homem do sexo masculino de {} anos e ele {}, gostou do produto'.format(idade, resposta))
else:
    print('foi entrevistado apenas uma mulher do sexo feminino de {} anos e ela {}, gostou do produto'.format(idade, resposta))
print('2) QUANTAS PESSOAS DISSERAM SIM E QUANTAS DISSERAM NÃO?') 
sleep(1)   
if resposta == 'SIM' :
    print(' Uma pessoa disse sim e zero pessoas disseram nao')
else:
    print(' Uma pessoa disse nao e zero pessoas disseram sim')
print('3) QUANTAS MULHERES DISSERAM SIM E QUANTOS HOMENS DISSERAM NÃO') 
sleep(1)
if sexo == 'F' and resposta == 'NAO':
    print('uma mulher disse não e nenhum homem disse não')
elif sexo == 'F' and resposta == 'SIM':
    print('uma mulher disse sim e nenhum homem disse não')    
elif sexo == 'M' and resposta == 'SIM':
    print('um homem disse sim e nenhuma mulher disse não')  
else:
    print('um homem disse não e nenhuma mulher disse sim')          
