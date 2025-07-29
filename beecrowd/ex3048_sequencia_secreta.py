N = int(input())
X = 0
cont = 0
for i in range(N):
    V = int(input())
    if X != V:
        cont += 1
        X = V
print(cont)