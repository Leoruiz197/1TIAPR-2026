texto1 = ""
texto2 = ""

with open('arquivo1.txt', 'r', encoding='UTF-8') as file:
    texto1 = file.read()

with open('arquivo2.txt', 'r', encoding='UTF-8') as file:
    texto2 = file.read()

with open('arquivo3.txt', 'w', encoding='UTF-8') as file:
    file.write(texto1)
    file.write("\n")
    file.write(texto2)