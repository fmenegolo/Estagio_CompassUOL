função, que recebe um único argumento e devolve para nós uma nova lista com a função aplicada a cada elemento da lista:
def func(arg):
    return arg + 2

lista = [2, 1, 0]

list(map(func, lista)) == [4, 3, 2] # true