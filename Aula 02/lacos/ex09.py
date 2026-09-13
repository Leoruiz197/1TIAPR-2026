soma = 0

num = int(input("Digite um número inteiro: "))

while num > 0:
    soma += num
    num = int(input("Digite outro número inteiro (ou um número negativo para sair): "))

print("A soma dos números positivos digitados é:", soma)