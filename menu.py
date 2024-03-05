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
    elif seleção == 2:
        a = input(int("Insira o primeiro numero"))
        b = input(int("Insira o segundo numero"))
        subtrair = calculadora.subtrair(a, b)
        print(f'{a} - {b} = {subtrair}')
    elif seleção == 3:
        a = input(int("Insira o primeiro numero"))
        b = input(int("Insira o segundo numero"))
        produto = calculadora.multiplicar(a, b)
        print(f'{a} * {b} = {produto}')
    elif seleção == 4:
        a = input(int("Insira o primeiro numero"))
        b = input(int("Insira o segundo numero"))
        quociente = calculadora.dividir(a, b)
        print(f'{a} + {b} = {quociente}')
    elif seleção == 0:
        print("Você saiu")
        break
    
    else:
        print("Opição invalida")
        break
        

    return

menu()