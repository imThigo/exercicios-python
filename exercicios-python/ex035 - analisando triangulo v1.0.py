print('{:=^21}'.format('Desafio 035'))
r1 = int(input('Digite o valor da primeira reta: '))
r2 = int(input('Digite o valor da segunda reta: '))
r3 = int(input('Digite o valor da terceira reta: '))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1: 
    print('Essas retas PODEM formar um triangulo')
else:
    print('Essas retas NÃO PODEM formar um triangulo')