import calculadora

def menu():
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicar")
    print("4. Dividir")
    print("0. Sair")
    seleção = input(int("Insira a opção desejada"))

    if seleção == 1:
        a = input(int("Insira o primeiro numero"))
        b = input(int("Insira o segundo numero"))
        soma = calculadora.somar(a, b)
        print(f'{a} + {b} = {soma}')
    elif seleção == 1:
        a = input(int("Insira o primeiro numero"))
        b = input(int("Insira o segundo numero"))
        subtrair = calculadora.subtrair(a, b)
        print(f'{a} - {b} = {subtrair}')
    
    return

menu()