def soma (a, b):
    return a + b
def multiplicacao (a, b):
    return c * d
def subtracao (a, b):
    return a - b
def divisao (a, b):
    return a / b
c = int(input('digite um numero:'))
d = int(input('digite um numero:'))
operacao = input('digite a operação:')

if operacao == 'soma':
    resultado = soma( c, d)
    print(f"o resultado é : {resultado} ")
elif operacao == 'multiplicacao':
    resultado = multiplicacao(c, d)
    print(f"o resultado é :{resultado} ")
elif operacao == 'subtracao':
    resultado = subtracao(c, d)
    print(f"o resultado é :{resultado} ")
elif operacao == 'divisao':
    resultado = divisao(c , d)
    print(f"o resultado é :{resultado} ")
else:
    print('operação invalida')
    