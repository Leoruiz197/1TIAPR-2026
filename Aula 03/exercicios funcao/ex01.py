def somar(num1, num2):
    return num1 + num2

def subtrair(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    return num1 / num2

def calculadora():
    num1 = float(input("digite o primeiro numero: "))
    num2 = float(input("digite o segundo numero: "))

    print(somar(num1,num2))
    print(subtrair(num1,num2))
    print(multiplicar(num1,num2))
    print(dividir(num1,num2))

calculadora()