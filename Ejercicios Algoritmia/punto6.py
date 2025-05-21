import random

lista = [random.randint(1, 100) for _ in range(20)]

print("Lista generada:")
print(lista)

num = int(input("Ingrese el número a buscar: "))

encontrado = False

for i in range(len(lista)):
    if lista[i] == num:
        print(f"Número encontrado en la posición: {i}")
        encontrado = True
        break

if not encontrado:
    print("Número no encontrado")