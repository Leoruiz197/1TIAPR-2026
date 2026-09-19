matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

nova_linha = [10, 11, 12]
matriz.append(nova_linha)

matriz[1].insert(0,100)

del matriz[1][2]

elemento = matriz[1].pop(2)
print(f"O elemento removido foi o {elemento}")

for linha in matriz:
    for elemento in linha:
        print(elemento, end = ' ')
    print()

# for linha in matriz:
#     print(linha)

# for l in range(len(matriz)):
#     for c in range(len(matriz[l])):
#         print(matriz[l][c])

matriz2 = [ [1, 2, 3] , [4, 5, 6] , [7, 8, 9] ]

matriz2[1][1] = 10