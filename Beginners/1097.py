I: int = 1
J: int = 7

while I <= 9:
    print(f'I={I} J={J}')
    print(f'I={I} J={J-1}')
    print(f'I={I} J={J-2}')

    I += 2
    J += 2