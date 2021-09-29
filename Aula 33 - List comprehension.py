c = [1, 2, 3, 4, 5]
d =[]

for i in c:
    d.append(i**2)

print(" Calculo normal :")
print(c)
print(d)    



a = [1, 2, 3, 4, 5]
b =[x**2 for x in a] #[valor_a_adcionar laço condição]
print(" Usando list comprehension : ")
print(a)
print(b)    




e = [1, 2, 3, 4, 5]
f =[y**2 for y in e] #[valor_a_adcionar laço condição]
g = [y for y in e if y%2==0]
print(" Usando list comprehension 2 numeros pares : ")
print(g)
