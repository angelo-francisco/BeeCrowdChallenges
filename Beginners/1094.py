N: int = int(input())

total: int = 0 
counts: dict[str, int] = {'R': 0, 'S': 0, 'C': 0}
percentual: dict[str, float] = {'R': 0, 'S': 0, 'C': 0}

for _ in range(N):
    quantity, animal = input().split()
    quantity = int(quantity)

    total += quantity
    
    if animal in counts:
        counts[animal] += quantity

for k in percentual.keys():
    percentual[k] = (100 * counts[k]) / total

print(f"Total: {total} cobaias")
print(f"Total de coelhos: {counts['C']}\nTotal de ratos: {counts['R']}\nTotal de sapos: {counts['S']}")
print(f"Percentual de coelhos: {percentual['C']:.2f} %\nPercentual de ratos: {percentual['R']:.2f} %\nPercentual de sapos: {percentual['S']:.2f} %")