DDD_LIST = [
    (61, 'Brasilia'),
    (71, 'Salvador'),
    (11, 'Sao Paulo'),
    (21, 'Rio de Janeiro'),
    (32, 'Juiz de Fora'),
    (19, 'Campinas'),
    (27, 'Vitoria'),
    (31, 'Belo Horizonte')
]

ddd = int(input())
exists = False

for _ddd in DDD_LIST:
    if _ddd[0] == ddd:
        ddd = _ddd[1]
        exists = True
        break

if exists:
    print(ddd)

else:
    print('DDD nao cadastrado')