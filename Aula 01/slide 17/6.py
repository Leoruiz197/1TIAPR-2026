# Solicitar que o usuário insira sua idade
idade = int(input("Digite sua idade: "))

# Verificar se a pessoa pode votar
if idade > 15:
    print("Você pode votar.")
else:
    print("Você ainda não pode votar.")
