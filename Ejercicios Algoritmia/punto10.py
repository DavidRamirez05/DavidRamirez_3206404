import random

numeros = [random.randint(1, 100) for _ in range(20)]

print("Lista original:", numeros)

media_total = sum(numeros) / len(numeros)
print("Media de todos los números (Ej. 10):", media_total)

mayor = max(numeros)
menor = min(numeros)
media_mayor_menor = (mayor + menor) / 2
print("Media entre el mayor y menor número (Ej. 11):", media_mayor_menor)

lista_invertida = numeros[::-1]
print("Lista invertida (Ej. 12):", lista_invertida)