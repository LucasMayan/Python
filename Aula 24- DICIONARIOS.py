meu_dicionario = {"A":"AMEIXA", "L": "LUCAS", "C": "CACHORRO", "B": "BOLA"}

print(meu_dicionario["A"]) # mostra todas as referencias no dicionario A
print(meu_dicionario["B"])
print(meu_dicionario["C"])
print(meu_dicionario["L"])

for chave in meu_dicionario: 
    print(chave+"-"+meu_dicionario[chave]) # mostra os valores de cada dicionario em seu respectivo lugar

for i in meu_dicionario.items(): # mostra os valores separados por virgula em seu respectivo lugar em resumo converte em banco de dados
    print(i)

for i in meu_dicionario.values(): # mostra somente os valores de cada dicionario
    print(i)

for i in meu_dicionario.keys(): # mostra os dicionarios na sequencia da variavel meu_dicionario
    print(i)

