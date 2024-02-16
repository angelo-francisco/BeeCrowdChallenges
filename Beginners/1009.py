nome = input()
salario = float(input())
vendas_dinheiro = float(input())

total = salario + ((15/100) * vendas_dinheiro)
print(f'TOTAL = R$ {total:.2f}')
