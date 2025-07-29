N = int(input())
L = []

for i in range(N):
    L.append(int(input()))

frequencia = {}

for i in L:
    if i in frequencia:
        frequencia[i] += 1
    else:
        frequencia[i] = 1

for i in sorted(frequencia.keys()):
    print(f'{i} aparece {frequencia[i]} vez(es)')