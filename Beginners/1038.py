code, quantity = map(int, input().split())

products = [
    [1, 4.00],
    [2, 4.50],
    [3, 5.00],
    [4, 2.00],
    [5, 1.50]
]

price = 0

for product in products:
    if code == product[0]:
        price = quantity * product[1]
        print(f'Total: R$ {price:.2f}')
        break