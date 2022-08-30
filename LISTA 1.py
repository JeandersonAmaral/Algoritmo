# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 22:35:46 2022

@author: Jeanderson

LISTA 1 DE ALGORITMO

"""

1. Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número]

n = float(input('Insira um número aqui: '))
print('O número informado foi: ', n)


2. Faça um Programa que peça dois números e imprima a soma.

n1 = float(input('Insira o primeiro número aqui: '))
n2 = float(input('Insira o segundo número aqui: '))
n3 = n1 + n2

print('A soma dos números é: ',n3)


3. Faça um Programa que peça 4 notas bimestrais e mostre a média.

n1 = float(input('Insira primeira nota aqui: '))
n2 = float(input('Insira segunda nota aqui: '))
n3 = float(input('Insira terceira nota aqui: '))
n4 = float(input('Insira quarta nota aqui: '))
m = (n1+n2+n3+n4)/4

print('A média é: ', m)


4. Faça um Programa que converta metros para centímetros.

m = float(input('Insira o valor em metros: '))
c = m*100
print('O valor de', m, 'metros em centimetros é:',c )


5. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área

r = float(input('Insira o valor do raio: '))
a = 3,14*(r**2)
print('A área do circulo é: ', a)  


6. Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área
para o usuário.

l1 = float(input('Insira a medida do primeiro lado: '))
l2 = float(input('Insira a medida do segundo lado: '))
a = l1*l2 
d = a*2
print('A area dos quadrado é: , ',a,' E o dobro da area é: ',d)


7. Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F
- Feminino, M - Masculino, Sexo Inválido.

s = str(input('Insira F para feminino e M para Masculino: '))

if s == 'F' or s == 'f': 
    print('F - Feminino')
elif s == 'M' or s == 'm':
    print('M - Masculino')
else:
    print('Sexo invalido...')
    
    
8. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input('Insira uma letra: ')

if letra == 'a':
    print('A letra' ,letra, 'é uma vogal!')
elif letra == 'a':
    print('A letra' ,letra, 'é uma vogal!')
elif letra == 'e':
    print('A letra' ,letra, 'é uma vogal!')
elif letra == 'i':
    print('A letra' ,letra, 'é uma vogal!')
elif letra == 'o':
    print('A letra' ,letra, 'é uma vogal!') 
elif letra == 'u':
    print('A letra' ,letra, 'é uma vogal!') 
else:
    print('A letra',letra, 'é uma consoante!')


9. Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a
média alcançada por aluno e apresentar:
1. A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
2. A mensagem "Reprovado", se a média for menor do que sete;
3. A mensagem "Aprovado com Distinção", se a média for igual a dez

n1 = float(input('Insira a primeira nota aqui: '))
n2 = float(input('Insira a segunda nota aqui: '))
m = (n1+n2)/2

if m >=7 and m <10:
    print('APROVADO')
elif m <7:
    print('REPROVADO')
elif m >=10:
    print('APROVADO COM DISTINÇÃO')


10. Faça um Programa que leia três números e mostre o maior deles.

n1 = float(input('Insira o primeiro número: '))
n2 = float(input('Insira o segundo número: '))
n3 = float(input('Insira o terceiro número: '))

if n1 > n2 and n1 > n3:
    print('O maior número é: ', n1)
elif n2 > n1 and n2 > n3:
    print('O maior número é: ', n2)
elif n3 > n1 and n3 > n2:
    print('O maior número é: ', n3)
 
    
11. Faça um Programa que leia três números e mostre o maior e o menor deles

n1 = float(input('Insira o primeiro número: '))
n2 = float(input('Insira o segundo número: '))
n3 = float(input('Insira o terceiro número: '))

if n1 > n2 and n1 > n3:
    print('O maior número é: ', n1)
elif n2 > n1 and n2 > n3:
    print('O maior número é: ', n2)
elif n3 > n1 and n3 > n2:
    print('O maior número é: ', n3)
    
if n1 < n2 and n1 < n3:
    print('O menor número é: ', n1)
elif n2 < n1 and n2 < n3:
    print('O menor número é: ', n2)
elif n3 < n1 and n3 < n2:
    print('O menor número é: ', n3)
 
    
12. Faça um programa que pergunte o preço de três produtos e informe qual produto você deve
comprar, sabendo que a decisão é sempre pelo mais barato.

p1 = float(input('Insira o valor do primeiro produto: '))
p2 = float(input('Insira o valor do segundo produto: '))
p3 = float(input('Insira o valor do terceiro produto: '))

if p1 < p2 and p1 < p3:
    print('Compre o primeiro produto, ele está mais barato!')
elif p2 < p3 and p2 < p1:
    print('Compre o segundo produto, ele está mais barato!')
else:
    print('Compre o terceiro produto, ele está mais barato!')
    
    
13. Faça um Programa que leia três números e mostre-os em ordem decrescente

lista = []

n1 = float(input('Insira o primeiro número aqui: '))
lista.append(n1)
n2 = float(input('Insira o segundo número aqui: '))
lista.append(n2)
n3 = float(input('Insira o terceiro número aqui: '))
lista.append(n3)

lista.sort(reverse=True)
print(lista)


14. Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-vespertino ou N-Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou
"Valor Inválido!", conforme o caso.

t = input('Em qual turno você estuda? \n Por favor digite: \n M - Para Matutino \n V - Para Vespertino \n N - Para Noturno \n  ')

if t == 'm' or t =='M':
    print('Bom dia!')
elif t == 'v' or t =='V':
    print('Boa Tarde!')
elif t == 'n' or t =='N':
    print('Boa Noite!')
else:
    print('Resposta Inválida!')
    
    
15. As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe
contraram para desenvolver o programa que calculará os reajustes.

1. Faça um programa que recebe o salário de um colaborador e o reajuste segundo o
seguinte critério, baseado no salário atual:
2. salários até R$ 280,00 (incluindo) : aumento de 20%
3. salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
4. salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
5. salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado,
informe na tela:
6. o salário antes do reajuste;
7. o percentual de aumento aplicado;
8. o valor do aumento;
9. o novo salário, após o aumento

sala = float(input('Informe o salario atual: R$'))

if sala <= 280:
    sala_nov = sala + (sala*0.20)
    print(' - O novo salário é: R$', sala_nov,'\n - O Salário anterior era: R$', sala,'\n - Houve um aumento de: R$', sala*0.20,'\n - Equivalente a 20% de R$', sala)
    
elif sala >= 280 and sala <= 700:
    sala_nov = sala + (sala*0.15)
    print(' - O novo salário é: R$', sala_nov,'\n - O Salário anterior era: R$', sala,'\n - Houve um aumento de: R$', sala*0.15,'\n - Equivalente a 15% de R$', sala)
    
elif sala >= 700 and sala <= 1500:
    sala_nov = sala + (sala*0.10)
    print(' - O novo salário é: R$', sala_nov,'\n - O Salário anterior era: R$', sala,'\n - Houve um aumento de: R$', sala*0.10,'\n - Equivalente a 10% de R$', sala)

elif sala >= 1500:
    sala_nov = sala + (sala*0.05)
    print(' - O novo salário é: R$', sala_nov,'\n - O Salário anterior era: R$', sala,'\n - Houve um aumento de: R$', sala*0.05,'\n - Equivalente a 05% de R$', sala)
    
    
16. Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do
Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato
e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que
deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa
deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
1. Desconto do IR:
2. Salário Bruto até 900 (inclusive) - isento
3. Salário Bruto até 1500 (inclusive) - desconto de 5%
4. Salário Bruto até 2500 (inclusive) - desconto de 10%
5. Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações,
dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de
hora é 220.
6. Salário Bruto: (5 * 220) : R$ 1100,00
7. (-) IR (5%) : R$ 55,00
8. (-) INSS ( 10%) : R$ 110,00
9. FGTS (11%) : R$ 121,00
10. Total de descontos : R$ 165,00
 Salário Liquido : R$ 935,00
 
fgts = 11
ir = 5
inss = 10
valor_hr = float(input('Informe o valor da sua hora trabalhada: '))
total_hr = float(input('Informe o total de horas trabalhadas no mês: '))

sb = valor_hr*total_hr
print('\n .......... RESUMO SALARIAL ..........')
print(' - Valor da hora trabalhada = R$',valor_hr,'\n - Horas trabalhadas no mês =',total_hr,'Hs' '\n - Total BRUTO = R$',sb)

calcir = sb*(ir/100)
print('\n - IR -- (5%) - R$',calcir)

calcinss = sb*(inss/100)
print(' - INSS -- (10%) - R$',calcinss)

calcfgts = sb*(fgts/100)
print(' - FGTS -- (11%) - R$',calcfgts, '\n - Total de desconto: R$',calcir + calcinss, '\n - Total LIQUIDO: R$',sb - calcir - calcinss)


