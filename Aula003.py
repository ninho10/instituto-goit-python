import math

# EX DE IF E ELSE

N1 = 10
N2 = 5
if (N1 > N2):
    print('o valor n1 e o maior')


Numero = int(input('Digite um numero '))
if (Numero > 20):
    print('Esse numero e maior que 20 maior')


Numero1 = int(input('Digite um numero '))
Numero2 = int(input('Digite segundo numero '))
Soma = Numero1 + Numero2
if (Soma > 10):
    print('{} e maior que 10 maior'.format(Soma))


numero = int(input('Digite um numero '))
if (numero % 3 == 0):
    print("entrou")


numero = int(input('Digite um numero '))
if (numero > 10):
    print("maior que 10")
else:
    print("menor que 10")


numero = int(input('Digite um numero '))
if (numero % 2 == 0):
    print("par")
else:
    print("imp")

numero = int(input('Digita um numero'))
if (numero % 5 == 0):
    print("sim")
else:
    print("nâo")

numero = int(input('Digita um numero '))
if ((numero >= 20) and (numero <= 90)):
    print("sim estar")
else:
    print("nâo Estar")


numero = int(input('Digita um numero '))
if (numero > 0):
    print(math.sqrt(numero))
else:
    print("numero ** 2")
