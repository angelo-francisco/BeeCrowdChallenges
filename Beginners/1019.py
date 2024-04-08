segundos = int(input(""))

minutos = segundos // 60
hora = minutos // 60

print(f"{hora}:{minutos % 60}:{segundos % 60}")
