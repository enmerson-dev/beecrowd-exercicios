entrada = input().split()
A, B, C = map(float, entrada)
A, B, C = sorted([A, B, C], reverse=True)
if A >= B + C:
    print('NAO FORMA TRIANGULO')
else:
    if A ** 2 == B ** 2 + C ** 2:
        print('TRIANGULO RETANGULO')
    elif A ** 2 > B ** 2 + C ** 2:
        print('TRIANGULO OBTUSANGULO')
    elif A ** 2 < B ** 2 + C ** 2:
        print('TRIANGULO ACUTANGULO')

    if A == B and B == C:
        print('TRIANGULO EQUILATERO')
    elif A == B or A == C or B == C:
        print('TRIANGULO ISOSCELES')