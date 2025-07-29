N = int(input())
for i in range(N):
    X = float(input())
    if X % 2 == 0:
        paridade = 'EVEN'
    else:
        paridade = 'ODD'
    if X > 0:
        sinal = 'POSITIVE'
        print(paridade, sinal)
    elif X == 0:
        sinal = 'NULL'
        print(sinal)
    else:
        sinal = 'NEGATIVE'
        print(paridade, sinal)