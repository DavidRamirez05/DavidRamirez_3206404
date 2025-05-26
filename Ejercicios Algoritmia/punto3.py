"""
3.Diseñar el algoritmo que encuentre (muestre) los números pares que hay entre el 100 y el 1000.
"""
print("Numeros pares del 100 y al 1000")
for i in range(100, 1001): 
    if i % 2 == 0:
        print(i)