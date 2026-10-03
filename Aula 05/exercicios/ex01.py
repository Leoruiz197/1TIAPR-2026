arq = input("digite o nome do arquivo que deseja contar as palavras: ")

with open(arq, "r", encoding = "UTF-8") as file:
    conteudo = file.read()
    palavras = conteudo.split()
    print(f"A quantidade de palavras no arquivo: {arq} é de {len(palavras)} palavras!")
