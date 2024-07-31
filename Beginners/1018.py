valor = int(input(''))
notas = [100, 50, 20, 10, 5, 2, 1]

print(valor)
if 0 < valor < 10**6:
    for nota in notas:
        num_notas = valor // nota
        nota_reais = str(format(nota, '.2f')).replace('.', ',')
        print(f'{num_notas} nota(s) de R$ {nota_reais}')

        valor -= num_notas*nota