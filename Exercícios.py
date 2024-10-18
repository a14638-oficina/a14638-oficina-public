ValorA = input("Insira um valor numérico") 
print(ValorA)

 #EX0.1 
""" 
Declara uma variável chamada "idade" e atribuiu a tua idade. Declara uma variável chamada "nome" e atribuiu o teu nome. Imprima no ecrã a frase "O meu nome é [nome] e tenho [idade] anos." 
""" 
idade = input ("Insira a sua idade: ") 
nome = input ("Insira o seu nome" ) 
print(f"O meu nome é {nome} e tenho {idade} anos")

 #EX0.2
"""
Escreve um programa que imprima "Olá, mundo!" no ecrã.
Cria uma variável chamada "fruta" e atribuiu o nome de uma fruta.
Imprime no ecrã a frase "Eu gosto de [fruta]."
"""
print("Olá Mundo!");
fruta = ("bananas");
print(f"Eu gosto de {fruta}")

#EX0.3
"""
Solicita ao utilizador para digitar o nome.
Imprime no ecrã uma saudação personalizada utilizando o nome fornecido.
Pede ao utilizador para digitar um número inteiro.
Imprime o dobro desse número.
"""
nome = input("Insira o seu nome: ")
print(f"Bom dia {nome}, eu espero que o seu dia esteja bom, se não melhoras.")
valor = int(input("Insira um número: "))
dobro = valor * 2 
print(f"o dobro de {valor} é {dobro}")

#EX1.1

"""
Elabora um programa que imprima a mensagem “Bem-vindos ao Python!”, precedida por uma linha em branco
"""

print ("\nBem-Vindos ao Python")

#EX1.2
"""
Elabora um programa que imprima a mensagem “José, bem-vindo ao Python!”, precedida por uma linha em branco
"""
nome = input("Insert your name: ")
print(f"\n Bem-Vindo ao python {nome}")

#EX1.3
"""
Elabora um programa que atribua a mensagem a uma variável e, em seguida, imprima o valor da variável.
"""
mensagem = """________                       ___    ______       _________                    
___  __ )___________ ___       __ |  / /__(_)____________  /_____________       
__  __  |  _ \_  __ `__ \________ | / /__  /__  __ \  __  /_  __ \_  ___/       
_  /_/ //  __/  / / / / //_____/_ |/ / _  / _  / / / /_/ / / /_/ /(__  )        
/_____/ \___//_/ /_/ /_/       _____/  /_/  /_/ /_/\__,_/  \____//____/         """
print(mensagem)

#EX1.4
"""
Elabora um programa que atribua o nome, a idade e a localidade de residência do aluno a três variáveis e imprima os valores dessas variáveis.
"""
nome = "Joaquim"
idade = int(16)
localidade = "Codessos"

print(f"{nome}, tem {idade} anos e reside em {localidade}")

#EX1.5
"""
EX1.5
Elabora um programa que intercale a designação da linguagem de programação e o nome do aluno na mensagem
"""
linguagemdeprog = "python"
nome = "Joaquim"

print(f"O {nome} sabe programar em {linguagemdeprog}")

#EX1.6
"""
EX1.6
Elabora um programa que alinhe à direita, à esquerda e ao centro a mensagem “Bem-vindo ao Python!” num campo de edição com 50 carateres.
"""

print(f"{'Bem vindo ao Python' : <50}")
print(f"{'Bem vindo ao Python' : ^50}")
print(f"{'Bem vindo ao Python' : >50}")

#EX1.7
"""
Elabora um programa que desenvolva o algoritmo de um programa que permita calcular o perímetro e área de uma circunferência a partir do valor do raio.
"""

raio = float(input("Digite o raio da circunferência: "))
perimetro = 2 * 3.14 * raio
area = 3.14*((raio)**2)
print("Uma círcunferência do raio:",raio,"unidades,")
print("tem um perimetro de:",perimetro,"unidades")
print("e área de:",area,"unidades")

#EX1.8
"""
Elabora um programa que imprima a data e horas correntes nos seguintes formatos:
02-10-2024
02-10-2024 16:11:20
10-02-2024 16:11:20
02/10/24
16:11:20
"""
from dataclasses import make_dataclass
import datetime
x = datetime.datetime.now()
dia = x.strftime("%d")
mes = x.strftime("%m")
ano = x.strftime("%y")
hora = x.strftime("%H")
minutos = x.strftime("%M")
segundos = x.strftime("%S")
print(f"{dia}-{mes}-{ano}")
print(f"{dia}-{mes}-{ano} {hora}:{minutos}:{segundos}")
print(f"{mes}-{dia}-{ano} {hora}:{minutos}:{segundos}")
print(f"{mes}/{dia}/{ano}")
print(f"{hora}:{minutos}:{segundos}")

#EX1.9
"""
Elabora um programa que leia o número mecanográfico de um atleta, assim como a sua pontuação. O número é inteiro e a pontuação final é real.
Digite o número do atleta: 12304
Digite a pontuação final: 7.89
O atleta número 12304 obteve 7.89 pontos.
"""
nda = input("Insira o número do atleta: ")
pda = input("Insira a pontuação final: ")

print(f"\nO atleta {nda} obteu {pda} pontos")

#EX.1.10
"""
Elabora um programa que leia a data de nascimento de uma pessoa e imprima a sua idade à data atual.
"""
import datetime
aniversario = input("Insira a sua data de aniversário: ")
dia,mes,

#EX.TPC
from types import NotImplementedType


nome = str(input('Qual é seu nome? '))
if nome == 'Joaquim':
  print('Que nome lindo tu tens!')
else:
  print('O teu nome é tão comum')
print('Bom dia, {}!'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2 )/2
print('A tua média foi {:.1f}'.format(m))
if m >= 6.0:
  print('A tua média foi boa! PARABÉNS!')
else:
  print('A tua média foi má! ESTUDA MAIS!')

#D28

import random

something = int(random.randint(0,5))
# print(f"o número secreto é: {something}")

numeroescolhido = int(input("Insira um valor entre (0 e 5): "))

if numeroescolhido > something:
  print("O número inserido é maior do que o eu!")
elif numeroescolhido < something:
  print("O número inserido é menor do que o meu!")
elif numeroescolhido == something:
  print("O número inserido é igual ao meu!!! ")
  print("PARABÉNS!!!")

#D29

velocidade = int(input("Insira a velocidade em que o motorista ia: "))
multa = velocidade - 80
valor = (multa) * 7
if velocidade > 80:
  print(f"Excedeste a velocidade em {multa}Km/h e vais ter que pagar {valor}€")
else:
  print("Estavas na velocidade certa!")

#EX.2
"""
Exercício FP1: Verificar se um número é positivo, negativo ou zero.
Escreve um programa em Python que peça ao utilizador para introduzir um número e verifica se ele é positivo, negativo ou igual a zero.
Dica: Usa as estruturas condicionais if, elif e else.

[consola]
Introduza um número: 10
O número é positivo.
"""

numero = int(input("Insira um número: "))
if numero == 0:
  print("O número inserido é zero!")
elif numero < 0:
  print("O número inserido é negativo!")
elif numero > 0:
  print("O número inserido é positivo!")

#EX.2.1
"""
Exercício FP2: Verificar se um número é par ou ímpar.
Escreve um programa que peça ao utilizador um número inteiro e verifica se ele é par ou ímpar.
Dica: Para verificar se um número é par, utilize a operação de módulo %.
[consola]
Introduza um número: 7
O número é ímpar.
"""

x = numero = int(input("Insira um número: "))
resultado = x % 2

if resultado == 0:
  print("O número inserido é Par!")
elif resultado == 1:
  print("O número inserido é Ímpar!")

#Exercício FP3: 
"""
Calcular a nota final de um aluno.
Elabora um programa que pergunte ao utilizador a nota final de um aluno e verifica a classificação de acordo com a seguinte tabela:

Nota inferior a 10: "Reprovado"
Nota entre 10 e 14: "Suficiente"
Nota entre 15 e 17: "Bom"
Nota superior a 17: "Muito Bom"

[consola]
Introduza a nota final: 16
Classificação: Bom
"""
notafinal = int(input("Insira a Nota final do aluno: "))

if notafinal < 10:
  print("REPROVADO")
elif notafinal >= 10 and notafinal <= 14:
   print("Suficiente")
elif notafinal >= 15 and notafinal < 17:
  print("Bom")
else:
  print("Muito Bom")

#EX.Casa

salariofinalmes = float(input("Insira a quantidade recebida de pagamento: "))

if salariofinalmes == 950:
  print("Valor correto a receber!")
else :
  if salariofinalmes < 950 or salariofinalmes > 950:
    print("Quantia incorreta de se receber!!!")

#EX.FP4
"""
Fórmulas:Exercício FP4: Conversor de temperaturas.
Cria um programa que pergunte ao utilizador uma temperatura em graus Celsius e a converta para Fahrenheit, Kelvin ou ambas. O utilizador deve escolher a unidade de destino (Fahrenheit ou Kelvin), e o programa deve exibir o valor convertido.



Fahrenheit = Celsius * 9/5 + 32
Kelvin = Celsius + 273.15
"""

celsius = float(input("Insira a temperatura em graus Celsius: "))
Fahrenheit = (celsius * 9/5) + 32
Kelvin = celsius + 273.15
opcao = str(input("Escolha a conversão para Fahrenheit(F), Kelvin(K) ou Ambas(A): "))

if opcao == "F": 
  print(f"O valor em Fahrenheit é {Fahrenheit}")
elif opcao == "K":
  print(f"O valor em Kelvin é {Kelvin}")
elif opcao == "A":
  print(f"O valor em Fahrenheit é {Fahrenheit} e em Kelvin é {Kelvin}")
else:
  print("Opção inserida invalida!!!")

#EX.FP5
"""
Exercício FP5: Cálculo de impostos
Crie um programa que peça ao utilizador o seu salário mensal e calcule o imposto de acordo com a seguinte tabela:

Salário até 1000: isento de impostos
Salário entre 1001 e 2000: 10% de imposto
Salário superior a 2001: 20% de imposto
O programa deve exibir o salário após a dedução do imposto.
"""

salario = float(input("Insira o salario mensal: "))

if salario <= 1000:
  print("Isento de imposto.")
elif salario > 1001 and salario <= 2000:
  imposto1 = salario * 0.10
  salarioImposto = salario - imposto1
  print(f"O salário com o imposto retirado é {salarioImposto}€")
elif salario >= 2001:
  imposto1 = salario * 0.20
  salarioImposto = salario - imposto1
  print(f"O salário com o imposto retirado é {salarioImposto :.2f}€")

#Ex.FP6: 
"""Imprimir números de 1 a 10.
Escreve um programa em Python que use um ciclo for para imprimir todos os números de 1 a 10.
"""

for X in range(1,11):
  print(X)

#Ex.FP7: 
"""
Escreve um programa que use um ciclo while para calcular a soma de todos os números de 1 a 100.

[consola]
A soma de 1 a 100 é: 5050
"""

soma = 0
contador = 1

while contador <= 100:
  soma += contador
  contador += 1

  print(f"A soma de 1 a 100 é: {soma} ")

#Ex FP8
"""
Escreve um programa que peça ao utilizador para introduzir uma frase e utilize um ciclo for para contar quantas vogais (a, e, i, o, u) existem na frase.

[consola]
Introduza uma frase: Programação em Python
Número de vogais: 7
"""

frase = (input("Insira uma frase: "))
vogais = 0

for letra in frase:
  if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u" == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
    vogais += 1

print (vogais)

#ExFP9
"""
Escreve um programa que utilize um ciclo for para listar todos os múltiplos de 5 entre 1 e 50.

[consola]
5
10
15
...
50
"""
temporario = 0

for i in range (1,51):
  if temporario <= 49:
    temporario = i * 5
    print(temporario)

#ExFP10
"""
Escreve um programa que crie uma lista de 5 números inteiros, pede ao utilizador para introduzir cada número e, em seguida, calcula e exibe a média desses números.

[consola]
Introduza o número 1: 10
Introduza o número 2: 20
Introduza o número 3: 30
Introduza o número 4: 40
Introduza o número 5: 50
A média é: 30.0
"""
notas = []
valor = 0
for i in range (1,6):

  num = int(input("Insira um número inteiro: "))
  notas.append (num)
print(notas)
for i in range(0,4):
  valor += notas[i]
int(valor1)
total = valor / 5
print(total)

#ExFP10
"""
Escreve um programa que crie uma lista de 5 números inteiros, pede ao utilizador para introduzir cada número e, em seguida, calcula e exibe a média desses números.

[consola]
Introduza o número 1: 10
Introduza o número 2: 20
Introduza o número 3: 30
Introduza o número 4: 40
Introduza o número 5: 50
A média é: 30.0
"""

notas = []
for i in range (0,5):
  numeros = int(input("Insira o valor inteiro: "))
  notas.append(numeros)
soma = sum(notas)
x = len(notas)
media = (soma / x )
print(media)

#ExFP11 

"""
Escreve um programa que peça ao utilizador um número inteiro e verifique se ele é primo. Um número primo é divisível apenas por 1 e por ele mesmo. O programa deve utilizar um ciclo for para testar se o número é divisível por algum outro número.
"""
numero = int(input('Insira um numero: '))
divisores = 0
for i in range(1, numero + 1 ):
    if numero % i == 0: #verifica se o resultado da divisão é 0
        divisores += 1  #incrementa o contador de divisores
if divisores  == 2:
    print(f"O {numero} é um número primo")
else:
    print(f"O {numero} não é um número primo")

#ExFP12
"""
Gerar uma lista de números pares.
Cria um programa que utilize a função range() e um ciclo for para gerar uma lista com todos os números pares entre 1 e 20 e imprima a lista.

[consola]
Lista de números pares: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
"""

list = []

for i in range(1,21):
  if i % 2 == 0:
    list.append(i)
print(f"Os números pares são: {list}")

#ExFP13
"""
Inverter uma string.
Escreve um programa que peça ao utilizador para introduzir uma palavra ou frase e utilize um ciclo para imprimir a string invertida.
"""
texto = str(input("Insira um texto: "))#Pedir o texto ao utilizador
textoinv = texto [::-1]#Script para inverter o texto
print (textoinv) #Printar o texto invertido

https://www.w3schools.com/python/numpy/numpy_array_slicing.asp 

#Ex.FP14
"""
Tabuada de multiplicação
Escreve um programa que gere a tabuada de multiplicação de um número introduzido pelo utilizador. O programa deve utilizar um ciclo for para calcular e exibir a tabuada até 10.

[consola]
Introduza um número: 6
Tabuada de 6:
6 x 1 = 6
6 x 2 = 12
...
6 x 10 = 60
"""
"""
num = int(input("Insira um valor inteiro: "))
for i in range (1,11):
  mult = num * i
  print(f"{num} x {i} = {mult}")
"""
num = int(input("Insira um valor inteiro: "))
i = 1
while i < 11:
  mult = num * i
  print(f"{num} x {i} = {mult}")
  i += 1

