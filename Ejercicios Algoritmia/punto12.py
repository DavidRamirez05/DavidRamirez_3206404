"""
12.Diseñar una solución que cree una lista inversa a la dada en 6. Es decir, que genere una nueva lista 
tal que su primer elemento sea el último de la lista inicial, su segundo elemento sea el penúltimo
de la lista inicial, etc.
"""
import random

lista_original = [random.randint(1, 100) for _ in range(20)]

print("Lista original:", lista_original)
lista_invertida = lista_original[::-1]
print("Lista invertida:", lista_invertida)