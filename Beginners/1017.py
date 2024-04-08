tempo_gasto = float(input(""))
velocidade = float(input(""))

distancia_percorrida = velocidade * tempo_gasto
litros_necessarios = distancia_percorrida / 12

print(f"{litros_necessarios:.3f}")
