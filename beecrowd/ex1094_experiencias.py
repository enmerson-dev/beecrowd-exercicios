N = int(input())
coelhos = ratos = sapos = 0

for i in range(N):
    entrada = input().split()
    quantia = int(entrada[0])
    tipo = entrada[1]
    match tipo:
        case 'C':
            coelhos += quantia
        case 'R':
            ratos += quantia
        case 'S':
            sapos += quantia
total = coelhos + ratos + sapos
print(f'Total: {total} cobaias')
print(f'Total de coelhos: {coelhos}')
print(f'Total de ratos: {ratos}')
print(f'Total de sapos: {sapos}')
print(f'Percentual de coelhos: {coelhos / total * 100:.2f} %')
print(f'Percentual de ratos: {ratos / total * 100:.2f} %')
print(f'Percentual de sapos: {sapos / total * 100:.2f} %')