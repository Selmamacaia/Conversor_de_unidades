lista = ['a', 'b', 'c']

try:
    elemento = lista.pop(1)
except IndexError:
    elemento = None
    print("Índice fora do intervalo da lista.")
if elemento is not None:
    print("Elemento removido:", elemento)