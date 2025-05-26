"""
21. Juego del Rojo-amarillo-verde: El programa genera cuatro dígitos aleatorios distintos entre 0 y 9. A estos dígitos se les asignan las posiciones 1, 2, 3 y 4. El objetivo del juego es adivinar los dígitos, así
como sus posiciones correctas en el menor número de intentos posibles. Para cada intento, el jugador proporciona tres dígitos para las posiciones 1, 2, 3 y 4. El programa responde con una pista
que consta de rojo, amarillo y verde. Si un dígito adivinado está en la posición correcta la respuesta es verde. Si el digito adivinado está en posición incorrecta, la respuesta es amarillo. Si el
dígito para una posición dada no coincide con ninguno de los cuatro dígitos, la respuesta es rojo.
"""
import random

def generar_codigo():
    return random.sample(range(10), 4)

def obtener_pista(intento, codigo):
    pista = []
    for i in range(4):
        if intento[i] == codigo[i]:
            pista.append("Verde")
        elif intento[i] in codigo:
            pista.append("Amarillo")
        else:
            pista.append("Rojo")
    return pista

def jugar():
    codigo = generar_codigo()
    intentos = 0

    print("Adivina el código secreto de 4 dígitos (0-9, sin repetir):")

    while True:
        intento_usuario = input("Ingresa 4 dígitos separados por espacio: ")

        if len(intento_usuario) != 4 or not all(x.isdigit() for x in intento_usuario):
            print("Entrada inválida. Intenta de nuevo.")
            continue

        intento = [int(x) for x in intento_usuario]
        if len(set(intento)) < 4:
            print("Los dígitos deben ser distintos.")
            continue

        intentos += 1
        pista = obtener_pista(intento, codigo)
        print("Pista:", pista)

        if pista == ["Verde"] * 4:
            print(f"¡Adivinaste el código {codigo} en {intentos} intentos!")
            break

jugar()
