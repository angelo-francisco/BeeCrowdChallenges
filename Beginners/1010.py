soma = 0
for i in range(0, 2):
    code, num_peca, valor_peca = input().split()
    soma += (int(num_peca) * float(valor_peca))

print(f'VALOR A PAGAR: R$ {soma:.2f}')