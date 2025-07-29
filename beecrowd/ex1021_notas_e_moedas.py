X = float(input())
X *= 100
N = int(X)

cem = N // 10000
N %= 10000

cinquenta = N // 5000
N %= 5000

vinte = N // 2000
N %= 2000

dez = N // 1000
N %= 1000

cinco = N // 500
N %= 500

dois = N // 200
N %= 200

um = N // 100
N %= 100

cent50 = N // 50
N %= 50

cent25 = N // 25
N %= 25

cent10 = N // 10
N %= 10

cent5 = N // 5
N %= 5

cent1 = N // 1
N %= 1

print('NOTAS:')
print(f'{cem} nota(s) de R$ 100.00')
print(f'{cinquenta} nota(s) de R$ 50.00')
print(f'{vinte} nota(s) de R$ 20.00')
print(f'{dez} nota(s) de R$ 10.00')
print(f'{cinco} nota(s) de R$ 5.00')
print(f'{dois} nota(s) de R$ 2.00')
print('MOEDAS:')
print(f'{um} moeda(s) de R$ 1.00')
print(f'{cent50} moeda(s) de R$ 0.50')
print(f'{cent25} moeda(s) de R$ 0.25')
print(f'{cent10} moeda(s) de R$ 0.10')
print(f'{cent5} moeda(s) de R$ 0.05')
print(f'{cent1} moeda(s) de R$ 0.01')