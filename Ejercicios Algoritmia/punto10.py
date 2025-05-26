"""
10.Con la lista del ejercicio 6, diseñar una solución que calcule la media de todos los números.
"""
import random

numeros = [random.randint(1, 100) for _ in range(20)]

print("Lista original:", numeros)

media_total = sum(numeros) / len(numeros)
print("Media de todos los números:", media_total)