# Solicitar que o usuário insira um ano
ano = int(input("Digite um ano: "))

# Verificar se o ano é bissexto
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("O ano", ano, "é bissexto.")
else:
    print("O ano", ano, "não é bissexto.")
