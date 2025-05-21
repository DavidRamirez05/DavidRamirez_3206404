import random

lista = [random.randint(1, 100) for _ in range(20)]

print("Lista generada:")
print(lista)

mayor = lista[0]
contador = 1

for i in range(1, len(lista)):
    if lista[i] > mayor:
        mayor = lista[i]
        contador = 1
    elif lista[i] == mayor:
        contador += 1

print(f"El numero mayor es: {mayor}")
print(f"Aparece {contador} veces.")