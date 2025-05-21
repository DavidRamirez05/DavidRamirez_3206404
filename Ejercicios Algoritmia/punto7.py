import random

lista = [random.randint(1, 100) for _ in range(20)]

print("Lista generada:")
print(lista)

num = int(input("Ingrese el número a buscar: "))

contador = 0
posiciones = []

for i in range(len(lista)):
    if lista[i] == num:
        contador += 1
        posiciones.append(i)

if contador > 0:
    print(f"El número {num} aparece {contador} veces.")
    print(f"Posiciones: {posiciones}")
else:
    print("Número no encontrado")