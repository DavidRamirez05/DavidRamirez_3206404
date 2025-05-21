import random

lista_original = [random.randint(1, 100) for _ in range(20)]

print("Lista original:", lista_original)

lista_invertida = lista_original[::-1]

print("Lista invertida:", lista_invertida)