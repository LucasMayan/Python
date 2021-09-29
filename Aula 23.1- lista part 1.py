minha_lista = ["abacaxi", "melância", "abacate"]
minha_lista_2 = [1,2,3,4,5]
minha_lista_3 = ["abacaxi", 2, 9.89, True]

print(minha_lista_3) # exibe o que a na minha_lista_3

print(minha_lista[2]) # exibe o que a na minha_lista_2 na posição 2

for item in minha_lista: # atribui a variavel item a minha_lista para exibir todos os valores dentro dela
    print(item) 

tamanho = len(minha_lista_3) # variavel tamanho usada para armazenar a contagem de item, função len é que faz a contagem   
print(tamanho) 

minha_lista.append("limao") # adciona a palavra limão na minha_lista

print(minha_lista)

if 7 in minha_lista_2: # procura pelo numero informado se existe na minha_lista_2
    print("7 está na lista")

del minha_lista[2:] # deleta todos os arquivos de minha_lista da posição 2 até o infinito
print(minha_lista)

del minha_lista[:] # deleta todos os arquivos de minha_lista
print(minha_lista)

