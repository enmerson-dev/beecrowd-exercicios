entrada = input().split()
L = []
L.append(int(entrada[0]))
L.append(int(entrada[1]))
L.append(int(entrada[2]))
ordenada = sorted(L)
for i in ordenada:
    print(i)
print()
for i in L:
    print(i)