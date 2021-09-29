# função reduce
from functools import reduce # importa a função reduce

def soma(x, y): # cria a função soma
    return x+y

lista = [1, 2, 4, 6, 20, 77]

soma = reduce(soma, lista)
print(soma)