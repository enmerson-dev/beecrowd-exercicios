carroX = 60
carroY = 90
distancia = int(input())
diferencaVELO = carroY - carroX
tempo = distancia / diferencaVELO * 60
print(f'{tempo:.0f} minutos')