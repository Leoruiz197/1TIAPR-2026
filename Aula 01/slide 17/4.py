# Solicitar que o usuário insira um caractere
caractere = input("Digite um caractere: ")

# Verificar se o caractere é uma vogal ou consoante
if caractere in ['a', 'e', 'i', 'o', 'u']:
        print("O caractere", caractere, "é uma vogal.")
else:
        print("O caractere", caractere, "é uma consoante.")