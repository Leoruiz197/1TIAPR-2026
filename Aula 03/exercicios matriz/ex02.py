matriz = [
    [1, 2],
    [3, 4]
]

escalar = 5

for l in range(len(matriz)):
    for c in range(len(matriz[l])):
        print(matriz[l][c]*escalar, end = " ")
    print()