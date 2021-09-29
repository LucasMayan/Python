arquivo = open("arquivo.txt")

linhas = arquivo.readlines()

print(linhas)

for linha in linhas :
    print(linha)

texto_completo = arquivo.read()

print(texto_completo)