def saudar(nome,idade):
    return f"Olá {nome}, idade: {idade}!"

print(saudar('Leo',12))
print(saudar('Jose',89))
print(saudar("thiago",34))
print(saudar("lucas",21))

def tratar_texto(texto):
    texto = texto.strip()
    texto = texto.lower()
    return texto

texto_ajustado = tratar_texto(input("Digite um texto: "))
print(texto_ajustado)
