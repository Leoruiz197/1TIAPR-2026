# Solicitar que o usuário insira um número
numero = float(input("Digite um número: "))

# Verificar se o número é positivo, negativo ou zero
if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")
