import random

tentativas = 3
num_certo = random.randint(1, 10)

while tentativas > 0:
    numero = int(input("Digite um número entre 1 e 10: "))
    if 1 <= numero <= 10:
        if numero == num_certo:
            print("Parabéns! Você acertou o número.")
            break
        else:
            tentativas -= 1
            print("Número incorreto. Tente novamente. Tentativas restantes:", tentativas)
            
    else:
        tentativas -= 1
        print(f"Número inválido! Você tem {tentativas} tentativas restantes.")  

if tentativas == 0:
    print("Suas tentativas acabaram. O número correto era:", num_certo)