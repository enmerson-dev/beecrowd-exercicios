X, Y = map(int, input().split())
while X != Y:
    print('Decrescente' if X > Y else 'Crescente')
    X, Y = map(int, input().split())