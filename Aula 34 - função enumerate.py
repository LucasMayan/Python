# função enumerate

lista = ["abacate", "bola", "cachorro"]

for i in range(len(lista)): # range vetor da variável, len mede o tamanho da variavel
    print(i, lista[i])

print("Função enumerate : ")
for x, nome in enumerate(lista):
    print(x, nome)