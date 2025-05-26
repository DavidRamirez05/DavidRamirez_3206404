"""
19.Dado un número entero, indicar el número de dígitos de ese número (para el 432 debe indicar 3)
"""
numero = int(input("Ingrese un número entero: "))
digitos = len(str(abs(numero)))

print(f"El número tiene {digitos} dígitos.")