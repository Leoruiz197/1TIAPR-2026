# Definir o preço do produto e a quantidade comprada
preco_unitario = 10  # Preço unitário do produto
quantidade = int(input("Digite a quantidade comprada: "))  # Quantidade comprada pelo usuário

# Calcular o preço total
if quantidade > 10:
    preco_total = quantidade * preco_unitario * 0.9  # Aplicar desconto de 10% para mais de 10 unidades
else:
    preco_total = quantidade * preco_unitario

# Exibir o preço total
print("O preço total a ser pago é R$", preco_total)
