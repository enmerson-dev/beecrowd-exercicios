N = int(input())
L = [N]
for i in range(1, 10):
    L.append(L[i - 1] * 2)
for i in range(len(L)):
    print(f'N[{i}] = {L[i]}')