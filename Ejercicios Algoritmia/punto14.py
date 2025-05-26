"""
14.Diseñar un algoritmo que cuente el número de palabras de un texto y el tamaño de la palabra más
grande. Una palabra puede venir separada de otra únicamente por un espacio. El texto se
ingresará por teclado.
"""
def Analizar():
    texto = input("Ingrese un texto: ").strip()
    palabras = texto.split()

    if len(palabras) == 0:
        print("No se ingresaron palabras.")
        return

    palabra_mas_larga = max(palabras, key=len)
    print(f"Número de palabras: {len(palabras)}")
    print(f"Longitud de la palabra más larga es: '{palabra_mas_larga}' con {len(palabra_mas_larga)} caracteres.")
Analizar()