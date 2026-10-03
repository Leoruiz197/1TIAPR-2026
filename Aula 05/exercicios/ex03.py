palavra = input("Digite a palavra a ser buscada: ")
existe = False

with open("texto.txt", "r", encoding="UTF-8") as file:
    linhas = file.readlines()
    for i, linha in enumerate(linhas,1):
        if palavra in linha:
            print(f"A palavra: {palavra} se encontra na linha num: {i}")
            existe = True
    if not existe:
        print("A palavra nao foi encontrada em nenhuma linha!")