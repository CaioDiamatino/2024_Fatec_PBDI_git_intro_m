import calculadora

def main():
    a = 2
    b = 3
    soma = calculadora.somar(a, b)
    print(f'{a} + {b} = {soma}')
    subtração = calculadora.subtrair(a,b)
    print(f'{a} - {b} = {subtração}')
    produto = calculadora.multiplicar(a, b)
    print(f'{a} * {b} = {produto}')
    quociente = calculadora.dividir(a, b)
    print(f'{a} / {b} = {quociente}')
main()