"""
22.El mismo del punto anterior, pero para aumentar la dificultad del juego, Solo se mostrará en lapista la cantidad de cartas en cada estado, pero no su posición.
"""
import random

def generar_codigo():
    return random.sample(range(10), 4) 

def obtener_pista(intento, codigo):
    verdes = 0
    amarillos = 0
    rojos = 0

    for i in range(4):
        if intento[i] == codigo[i]:
            verdes += 1
        elif intento[i] in codigo:
            amarillos += 1
        else:
            rojos += 1

    return verdes, amarillos, rojos

def jugar():
    codigo = generar_codigo()
    intentos = 0

    print("Adivina el código secreto de 4 dígitos (0-9, sin repetir).")
    print("Pista: solo se te dirá cuántos verdes, amarillos y rojos hay (no las posiciones).")

    while True:
        intento_usuario = input("Ingresa 4 dígitos: ")

        if len(intento_usuario) != 4 or not all(x.isdigit() for x in intento_usuario):
            print("Entrada inválida. Intenta de nuevo.")
            continue

        intento = [int(x) for x in intento_usuario]
        if len(set(intento)) < 4:
            print("Los dígitos deben ser distintos.")
            continue

        intentos += 1
        verdes, amarillos, rojos = obtener_pista(intento, codigo)

        print(f"Pista: {verdes} verdes, {amarillos} amarillos, {rojos} rojos")

        if verdes == 4:
            print(f"¡Adivinaste el código {codigo} en {intentos} intentos!")
            break

jugar()
