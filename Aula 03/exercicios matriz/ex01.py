matriz1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

matriz2 = [
    [11,21,31],
    [41,51,61],
    [71,81,91]
]

for l in range(len(matriz1)):
    for c in range(len(matriz1[l])):
        soma = matriz1[l][c] + matriz2[l][c]
        print(soma, end = " ")
    print()