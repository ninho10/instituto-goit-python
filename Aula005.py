# Programa que ler salaria, sexo e idade e responde media de salario.
sexo = 0
idade = 0
salario = 0

salarioT = 0
FemininoCem = 0
media = 0
cont = 0

while idade >= 0:
    cont = cont + 1
    sexo = int(input('sexo [1]Masculino, [2]feminino --> '))

    salario = int(input('qual e seu salario --> '))
    salarioT = salarioT + salario
    if (sexo == 2) and (salario < 100):
        FemininoCem = FemininoCem + 1

    idade = int(input('qual e sua idade --> '))

media = salarioT / cont

print(f'a media do salario e {media}')
print(f'quantidade de mulher ganhando menos que 100 e {FemininoCem}')
