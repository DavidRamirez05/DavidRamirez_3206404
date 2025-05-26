"""
6.Dada en una lista no ordenada de números (20 enteros generados aleatoriamente) y un número
leído por teclado, diseñar una solución que busque en la lista el número leído. Si lo encuentra,
debe informar su posición en la lista, sino debe devolver la frase “Número no encontrado”.
"""
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