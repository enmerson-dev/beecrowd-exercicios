L = []
N = int(input())
for i in range(N):
    entrada = input().split()
    if entrada[0] == 'Thor':
        R = 'Y'
    else:
        R = 'N'
    L.append(R)
for i in L:
    print(i)