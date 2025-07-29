N = int(input())
L = []
for i in range(N):
    entrada = input().split()
    A = float(entrada[0])
    B = float(entrada[1])
    C = float(entrada[2])
    media = ((A * 2) + (B * 3) + (C * 5)) / 10
    L.append(media)
for i in L:
    print(f'{i:.1f}')