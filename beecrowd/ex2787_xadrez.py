L = int(input())
C = int(input())
if L % 2 == 0 and C % 2 == 0 or L % 2 != 0 and C % 2 != 0:
    cor = 1
else:
    cor = 0
print(cor)