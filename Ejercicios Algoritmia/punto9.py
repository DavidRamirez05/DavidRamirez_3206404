import random

lista = [random.randint(1, 100) for _ in range(20)]
print("Lista generada:")
print(lista)

num = int(input("Ingrese un número: "))

mayor = lista[0]
veces_mayor = 1 if lista[0] == mayor else 0
veces_num = 1 if lista[0] == num else 0

for i in range(1, len(lista)):
    if lista[i] > mayor:
        mayor = lista[i]
        veces_mayor = 1
    elif lista[i] == mayor:
        veces_mayor += 1

    if lista[i] == num:
        veces_num += 1

if veces_num > veces_mayor:
    print("Verdadero")
else:
    print("Falso")