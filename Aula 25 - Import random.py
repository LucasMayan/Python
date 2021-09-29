import random

# random.seed(1) # define a escolha de numero aleatorio como vetor 2
numero = random.randint(0, 10) # gera um numero aleatorio
print(numero)

lista = [6, 4 , 5 , 7, 45]
numero = random.choice(lista) # gera um numero aleatorio
print(numero)