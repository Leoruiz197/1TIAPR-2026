nome = input("Digite seu nome: ")

with open('meuarquivo.txt','w',encoding = "utf-8") as file:
    file.write('Olá, mundo!\n')
    file.write('Este é um arquivo de texto.\n')
    file.write(f'Criado por {nome}.')