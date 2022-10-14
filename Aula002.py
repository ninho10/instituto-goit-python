# 1 Faça um programa em Phyton que leia duas variáveis A e B.Aseguir,calcule o produto entre elas e atribua à variável PROD.
# A seguir mostre a variável PROD commensagem correspondente.

A = int(input('digite um valor '))
B = int(input('digite um valor '))
PROD = A + B
print('O resultado é ', PROD)


# 2 Faça um programa em Phyton que leia 2 variáveis A e B,que correspondem a 2 notas de um aluno.Aseguir,calcule a média do aluno,
# sabendo que anota A tempeso2, 5 e anota B tempeso 7,5.OBS.:Peso significa porcentagem.

A = float(input('digite um valor '))
B = float(input('digite um valor '))
Media1 = A * 0.75
Media2 = B * 0.25
print(Media1, Media2)


# 3 Faça um programa em Phyton que leia 3 variáveis A e B e C,que são as notas de um aluno.Aseguir,calcule a média do aluno,
# sabendo que a notaA tempeso2,anotaB tempeso3 e anotaC tempeso5.

Nota1 = float(input('digite um valor '))
Nota2 = float(input('digite um valor '))
Nota3 = float(input('digite um valor '))
Media1 = Nota1 * 0.20
Media2 = Nota2 * 0.30
Media3 = Nota3 * 0.50
print(Media1, Media2, Media3)


# 4Faça um programa em Phyton que leia 4 variáveis A,B,C e D.Aseguir,calcule e mostre adiferença do produtodeAeBpelo
# produtodeCeD(A*B-C*D).

A = float(input('digite um valor '))
B = float(input('digite um valor '))
C = float(input('digite um valor '))
D = float(input('digite um valor '))
Resultado = (A*B) - (C*D)

print(Resultado)


# 6 Escreva um programa em Phyton que leia a idade,emanos,deumapessoa,calcule e exiba o número de dias que uma pessoa já viveu.
# Considerequeummêstenha30dias.

Idade = int(input('digite sua idade '))
Resultado = (Idade * 365)
print(Resultado)
