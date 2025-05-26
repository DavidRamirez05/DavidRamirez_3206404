"""
16.Escribir el algoritmo que devuelve el cambio de las máquinas de la cafetería. La máquina solo
devuelve monedas de 1000, 500, 200, 100, 50. Se debe ingresar el valor a cobrar y el monto
entregado.
"""
def cambio():
    try:
        valor = int(input("Ingrese el valor a cobrar: "))
        pagado = int(input("Ingrese el monto entregado: "))

        if pagado < valor:
            print("El monto entregado es insuficiente.")
            return

        cambio = pagado - valor
        print(f"El cambio a devolver es de: {cambio}")

        monedas = [1000, 500, 200, 100, 50]
        cantidad = [0] * len(monedas)

        i = 0
        while cambio > 0 and i < len(monedas):
            cantidad[i] = cambio // monedas[i]
            cambio %= monedas[i]
            i += 1

        for i in range(len(monedas)):
            if cantidad[i] > 0:
                print(f"{cantidad[i]} monedas de {monedas[i]}")
    except:
        print("Entrada inválida.")
cambio()