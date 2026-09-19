matriz = [
    [1, 2],
    [3, 4],
    [5, 6]
]

transposta = [[0, 0, 0],
              [0, 0, 0]]

for l in range(3):
    for c in range(2):
        transposta[c][l] = matriz[l][c]


print("Matriz transposta: ")
for linha in transposta:
    print(linha)