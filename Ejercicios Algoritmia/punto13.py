import random

# Ejercicio 6: Generar lista de 20 enteros aleatorios
numeros = [random.randint(1, 100) for _ in range(20)]

def mostrar_lista():
    print("\nLista actual:", numeros)

# Ejercicio 6: Buscar un número
def buscar_numero():
    mostrar_lista()
    buscado = int(input("Ingrese el número a buscar: "))
    if buscado in numeros:
        print(f"Número encontrado en la posición: {numeros.index(buscado)}")
    else:
        print("Número no encontrado")

# Ejercicio 7: Contar cuántas veces aparece el número
def contar_apariciones():
    mostrar_lista()
    buscado = int(input("Ingrese el número a contar: "))
    veces = numeros.count(buscado)
    print(f"El número {buscado} aparece {veces} veces")

# Ejercicio 8: Contar cuántas veces aparece el número mayor
def contar_mayor():
    mayor = max(numeros)
    veces = numeros.count(mayor)
    print(f"El número mayor es {mayor} y aparece {veces} veces")

# Ejercicio 9: Verificar si un número aparece más veces que el mayor
def comparar_apariciones_con_mayor():
    mostrar_lista()
    buscado = int(input("Ingrese el número a comparar: "))
    veces_buscado = numeros.count(buscado)
    mayor = max(numeros)
    veces_mayor = numeros.count(mayor)
    if veces_buscado > veces_mayor:
        print("Verdadero: el número aparece más veces que el mayor")
    else:
        print("Falso: el número no aparece más veces que el mayor")

# Ejercicio 10: Media de todos los números
def media_total():
    promedio = sum(numeros) / len(numeros)
    print(f"La media de todos los números es: {promedio:.2f}")

# Ejercicio 11: Media entre el mayor y el menor
def media_entre_mayor_y_menor():
    mayor = max(numeros)
    menor = min(numeros)
    media = (mayor + menor) / 2
    print(f"Mayor: {mayor}, Menor: {menor}, Media entre ambos: {media:.2f}")

# Ejercicio 12: Lista invertida
def lista_invertida():
    invertida = numeros[::-1]
    print("Lista invertida:", invertida)

# Mostrar menú
def mostrar_menu():
    print("\n--- MENÚ DE OPCIONES ---")
    print("1. Buscar número en la lista (Ejercicio 6)")
    print("2. Contar cuántas veces aparece un número (Ejercicio 7)")
    print("3. Contar cuántas veces aparece el número mayor (Ejercicio 8)")
    print("4. Comparar número vs el mayor (Ejercicio 9)")
    print("5. Calcular la media de todos los números (Ejercicio 10)")
    print("6. Calcular la media entre el mayor y el menor (Ejercicio 11)")
    print("7. Mostrar lista invertida (Ejercicio 12)")
    print("8. Salir")

# Bucle principal del menú
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción (1-8): ")

    if opcion == '1':
        buscar_numero()
    elif opcion == '2':
        contar_apariciones()
    elif opcion == '3':
        contar_mayor()
    elif opcion == '4':
        comparar_apariciones_con_mayor()
    elif opcion == '5':
        media_total()
    elif opcion == '6':
        media_entre_mayor_y_menor()
    elif opcion == '7':
        lista_invertida()
    elif opcion == '8':
        print("Programa finalizado.")
        break
    else:
        print("Opción inválida. Intente de nuevo.")