lista = [4,7,2,7,9,3]

def media_lista(lista):
    soma = 0
    for num in lista:
        soma += num

    return soma / len(lista)

print(f"A media da lista é {media_lista(lista):.2f}")