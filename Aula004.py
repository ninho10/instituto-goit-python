# escreva 6 idade e fale a media das idades.

n1 = 0
totalI = 0
i = 0
while i < 6:
    i = i + 1
    n1 = input('Qual e seu Nome --> ')
    idade = int(input('qual e sua idade --> '))
    totalI = totalI + idade
media = totalI / 6
print(f'A media da idade e {media}')
