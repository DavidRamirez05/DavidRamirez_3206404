print ("Suma de pares que hay entre dos números")

n1 = int(input ("Digite su numero:"))
n2 = int(input ("Digite su numero:"))

if n1 > n2:
    n1, n2 = n2, n1 
    
suma = 0 
if n1 <= n2:
    for num in range(n1, n2 + 1):
        if num % 2 == 0:
            suma += num

print(f"La suma de los números pares entre {n1} y {n2} es: {suma}") 