idade_dias = int(input(''))

idade_anos = idade_dias // 365
idade_dias -= idade_anos * 365
idade_meses = idade_dias // 30
idade_dias -= idade_meses * 30

print(f'{idade_anos} ano(s)')
print(f'{idade_meses} mes(es)')
print(f'{idade_dias} dia(s)')
