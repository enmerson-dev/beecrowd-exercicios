N = int(input())
contador = 0
for i in range(N):
    X, Y = map(int, input().split())
    if Y > X:
        for j in range(X + 1, Y):
            if j % 2 != 0:
                contador += j
        print(contador)
        contador = 0
    else:
        for j in range(Y + 1, X):
            if j % 2 != 0:
                contador += j
        print(contador)
        contador = 0