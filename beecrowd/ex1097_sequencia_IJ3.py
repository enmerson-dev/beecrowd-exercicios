inicio = 7
fim = 4
for i in range(1 , 10, 2):
    for j in range(inicio, fim, -1):
        print(f'I={i} J={j}')
    inicio += 2
    fim = inicio - 3