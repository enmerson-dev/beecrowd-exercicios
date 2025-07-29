entrada = input().split()

A = float(entrada[0])
B = float(entrada[1])
C = float(entrada[2])

pi = 3.14159

triangulo = (A * C) / 2           # Base * Altura / 2
circulo = (C ** 2) * pi           # pi * Raio ** 2
trapezio = ((A + B) * C) / 2      # Base maior + Base menor * Altura / 2
quadrado = B * B                  # Lado * Lado
retangulo = A * B                 # Base * Altura

print(f'TRIANGULO: {triangulo:.3f}')
print(f'CIRCULO: {circulo:.3f}')
print(f'TRAPEZIO: {trapezio:.3f}')
print(f'QUADRADO: {quadrado:.3f}')
print(f'RETANGULO: {retangulo:.3f}')