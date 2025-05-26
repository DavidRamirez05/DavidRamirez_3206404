"""
13.Integre los ejercicios del 6 al 12, de tal manera que se presente un menú con las diferentes
opciones, el usuario escogerá una, ejecutando el procedimiento correspondiente y presentando
de nuevo el menú. Agregue una opción para finalizar la ejecución
"""
import random

lista = [random.randint(1, 10) for _ in range(20)]

def buscar_numero():
    num = int(input("Ingrese el número a buscar: "))
    if num in lista:
        print(f"El número {num} se encuentra en la posición {lista.index(num)}")
    else:
        print("Número no encontrado.")

def contar_numero():
    num = int(input("Ingrese el número a contar: "))
    conteo = lista.count(num)
    if conteo > 0:
        print(f"El número {num} aparece {conteo} veces.")
    else:
        print("Número no encontrado.")

def mayor_y_cuantas_veces():
    mayor = max(lista)
    conteo = lista.count(mayor)
    print(f"El número mayor es {mayor} y aparece {conteo} veces.")

def comparar_apariciones():
    num = int(input("Ingrese el número: "))
    mayor = max(lista)
    veces_num = lista.count(num)
    veces_mayor = lista.count(mayor)
    if veces_num > veces_mayor:
        print("Verdadero: el número aparece más veces que el mayor.")
    else:
        print("Falso: el número no aparece más veces que el mayor.")

def calcular_media():
    media = sum(lista) / len(lista)
    print(f"La media de todos los números es: {media}")

def media_mayor_menor():
    mayor = max(lista)
    menor = min(lista)
    media = (mayor + menor) / 2
    print(f"La media entre el mayor ({mayor}) y el menor ({menor}) es: {media}")

def lista_invertida():
    inversa = lista[::-1]
    print("Lista invertida:", inversa)

def mostrar_lista():
    print("Lista actual:", lista)

while True:
    print("\n----- MENÚ -----")
    print("1. Buscar un número en la lista")
    print("2. Contar cuántas veces aparece un número")
    print("3. Buscar el número mayor y cuántas veces aparece")
    print("4. Verificar si un número aparece más que el mayor")
    print("5. Calcular la media de todos los números")
    print("6. Calcular la media entre el mayor y el menor")
    print("7. Crear lista invertida")
    print("8. Mostrar lista actual")
    print("0. Salir")

    try:
        opcion = int(input("Seleccione una opción: "))
    except:
        print("Opción inválida.")
        continue

    if opcion == 0:
        print("Programa finalizado.")
        break
    elif opcion == 1:
        buscar_numero()
    elif opcion == 2:
        contar_numero()
    elif opcion == 3:
        mayor_y_cuantas_veces()
    elif opcion == 4:
        comparar_apariciones()
    elif opcion == 5:
        calcular_media()
    elif opcion == 6:
        media_mayor_menor()
    elif opcion == 7:
        lista_invertida()
    elif opcion == 8:
        mostrar_lista()
    else:
        print("Opción inválida.")