salario = float(input())
reajuste = 0
percentual = 0
if 0 <= salario <= 400:
    percentual = 0.15
    reajuste = salario * percentual
    salario += reajuste
elif 400 < salario <= 800:
    percentual = 0.12
    reajuste = salario * percentual
    salario += reajuste
elif 800 < salario <= 1200:
    percentual = 0.10
    reajuste = salario * percentual
    salario += reajuste
elif 1200 < salario <= 2000:
    percentual = 0.07
    reajuste = salario * percentual
    salario += reajuste
else:
    percentual = 0.04
    reajuste = salario * percentual
    salario += reajuste
print(f'Novo salario: {salario:.2f}')
print(f'Reajuste ganho: {reajuste:.2f}')
print(f'Em percentual: {percentual * 100:.0f} %')