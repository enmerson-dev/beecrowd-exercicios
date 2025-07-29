nota = int(input())
if nota == 0:
    conceito = 'E'
elif 0 < nota <= 35:
    conceito = 'D'
elif 35 < nota <= 60:
    conceito = 'C'
elif 60 < nota < 85:
    conceito = 'B'
else:
    conceito = 'A'
print(conceito)