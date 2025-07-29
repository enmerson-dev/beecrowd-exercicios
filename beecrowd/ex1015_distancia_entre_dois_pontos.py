entrada1 = input().split()
entrada2 = input().split()

x1 = float(entrada1[0])
y1 = float(entrada1[1])
x2 = float(entrada2[0])
y2 = float(entrada2[1])

distancia = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5 # ou import math, métod math.sqrt()
print(f'{distancia:.4f}')