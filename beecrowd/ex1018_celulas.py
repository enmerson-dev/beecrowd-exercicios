N = int(input())
valor_original = N
cem = 0
cinquenta = 0
vinte = 0
dez = 0
cinco = 0
dois = 0
um   = 0
while N >= 100:
    cem += 1
    N -= 100
while N >= 50:
    cinquenta += 1
    N -= 50
while N >= 20:
    vinte += 1
    N -= 20
while N >= 10:
    dez += 1
    N -= 10
while N >= 5:
    cinco += 1
    N -= 5
while N >= 2:
    dois += 1
    N -= 2
while N >= 1:
    um += 1
    N -= 1
print(f'{valor_original}')
print(f'{cem} nota(s) de R$ 100,00')
print(f'{cinquenta} nota(s) de R$ 50,00')
print(f'{vinte} nota(s) de R$ 20,00')
print(f'{dez} nota(s) de R$ 10,00')
print(f'{cinco} nota(s) de R$ 5,00')
print(f'{dois} nota(s) de R$ 2,00')
print(f'{um} nota(s) de R$ 1,00')