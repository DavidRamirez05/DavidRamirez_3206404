"""
18.Escriba un algoritmo que calcule la letra de control para el NIT. Se pedirá el NIT y escribirá por
pantalla la letra correspondiente. Para calcularlo, se obtiene el resto de dividir el número de NIT
entre 23, y se utiliza la siguiente tabla:
"""
tabla_letras = [
    'T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B',
    'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E'
]

nit = int(input("Ingrese el número de NIT: "))
resto = nit % 23
letra_control = tabla_letras[resto]

print(f"La letra de control para el NIT {nit} es: {letra_control}")