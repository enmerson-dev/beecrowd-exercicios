entrada = input().split()
H = int(entrada[0])
Z = int(entrada[1])
L = int(entrada[2])

if Z < H < L or L < H < Z:
    print('huguinho')
elif H < Z < L or L < Z < H:
    print('zezinho')
else:
    print('luisinho')