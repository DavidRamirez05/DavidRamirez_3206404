"""
15.Algoritmo que indica si un año es bisiesto. Un año es bisiesto si es divisible por cuatro, excepto
cuando es divisible por 100, a no ser que sea divisible por 400. Así, 1900 no fue bisiesto, pero 2000
sí lo fue.
"""
def bisiesto():
    try:
        año = int(input("Ingrese un año: "))
        if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
            print(f"{año} es un año bisiesto.")
        else:
            print(f"{año} no es un año bisiesto.")
    except:
        print("Entrada inválida.")
bisiesto()