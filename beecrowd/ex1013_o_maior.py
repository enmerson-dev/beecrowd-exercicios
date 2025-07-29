entrada = input().split()
numeros = [int((entrada[0])), int(entrada[1]), int(entrada[2])]

for i in range (len(numeros)):
    if numeros[i] < 0:
        numeros[i] = numeros[i] * (-1)
numeros_ordenados = sorted(numeros)
maiorAB = numeros_ordenados[2]
print(f'{maiorAB} eh o maior')