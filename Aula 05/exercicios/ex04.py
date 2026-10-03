lista_ordenada = []

with open('nomes.txt', 'r', encoding='UTF-8') as file:
    linhas = file.readlines()
    lista_ordenada = sorted(linhas)

with open('nomes_ordenados.txt', 'w', encoding='UTF-8') as file:
    for linha in lista_ordenada:
        file.write(linha)