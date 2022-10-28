# Digite 3 nomes bote dentro de uma lista e me der o maior nome
nomes = []
i = 0
for i in range(0, 3):
    nome1 = input('digita um nome --> ')
    nomes.append(nome1)
    print(nomes)
    print(max(nomes))
