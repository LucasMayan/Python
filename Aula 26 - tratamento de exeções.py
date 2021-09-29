a = 2
b = 0

try: # realiza um tratamento de condição
    print(a/b)
except: # caso realize o tratamento de condição e o valor for incoerente executa essa excessão para não travar o codigo
    print("Não é permitido divisão por 0")

print(a/a)