N = int(input())
for i in range(N):
    entrada = input().split()
    X = int(entrada[0])
    Y = int(entrada[1])
    try:
        R = X / Y
        print(R)
    except ZeroDivisionError:
        print('divisao impossivel')