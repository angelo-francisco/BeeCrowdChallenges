def calc_tax(value):
    tax = 0

    if value > 4500:
        tax += (value - 4500) * 0.28
        value = 4500
    
    if value > 3000:
        tax += (value - 3000) * 0.18
        value = 3000
    
    if value > 2000:
        tax += (value - 2000) * 0.08

    return tax


sallary = float(input())

tax = calc_tax(sallary)

if tax == 0:
    print('Isento')

else:
    print(f'R$ {tax:.2f}')