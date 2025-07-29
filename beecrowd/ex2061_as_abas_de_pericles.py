entrada = input().split()
abas = int(entrada[0])
acoes = int(entrada[1])

for i in range(acoes):
    situacao = input()
    if situacao == 'fechou':
        abas += 1
    elif situacao == 'clicou':
        abas -= 1
print(abas)