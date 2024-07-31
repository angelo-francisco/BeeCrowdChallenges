valor = float(input('')) * 100

_notas = [100, 50, 20, 10, 5, 2]
notas = [x * 100 for x in _notas]

_moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]
moedas = [x * 100 for x in _moedas]

if 0 <= valor <= pow(10, 6):
    print('NOTAS:')
    for nota in notas:
        res = divmod(valor, nota)[0]
        print(f'{int(res)} nota(s) de R$ {nota/100:.2f}')
        valor = valor % nota

    print('MOEDAS:')    
    for moeda in moedas:
        res = divmod(valor, moeda)[0]
        print(f'{int(res)} moeda(s) de R$ {moeda/100:.2f}')
        valor = valor % moeda