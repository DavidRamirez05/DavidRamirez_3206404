"""
11.Con la lista del ejercicio 6, Diseñar una solución que calcule la media entre el mayor y el menor.
"""
import random

numeros = [random.randint(1, 100) for _ in range(20)]
print("Lista generada:", numeros)

mayor = max(numeros)
menor = min(numeros)

media_mayor_menor = (mayor + menor) / 2

print("Mayor:", mayor)
print("Menor:", menor)
print("Media entre el mayor y menor:", media_mayor_menor)