with open('meuarquivo.txt','r',encoding = "utf-8") as file:
    conteudo = file.read()
    print(conteudo)

with open('meuarquivo.txt','r',encoding = "utf-8") as file:
    for linha in file.readlines():
        print(linha)