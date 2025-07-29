from math import sqrt
entrada = input().split()

A = float(entrada[0])
B = float(entrada[1])
C = float(entrada[2])

delta = (B * B) - (4 * A * C)

if A == 0:
    print('Impossivel calcular')
elif delta < 0:
    print('Impossivel calcular')
else:
    x1 = (-B + (sqrt(delta))) / (2 * A)
    x2 = (-B - (sqrt(delta))) / (2 * A)
    print(f'R1 = {x1:.5f}')
    print(f'R2 = {x2:.5f}')