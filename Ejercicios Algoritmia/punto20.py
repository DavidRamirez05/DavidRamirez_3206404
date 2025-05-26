"""
20.Calcular los pagos mensuales de una hipoteca y el total a pagar. El programa debe solicitar elcapital, el interés anual y el número de años y debe escribir la cuota a pagar mensualmente. Para
calcular la cuota se utiliza la siguiente fórmula: Sea C el capital del préstamo, R la tasa de interésmensual y N el número de pagos. La cuota mensual viene dada por: y el interés mensual = interés anual/100/12
"""
def calcular_cuota_mensual(capital, interes_anual, años):
    R = interes_anual / 100 / 12 
    N = años * 12
    if R == 0:
        cuota = capital / N 
    else:
        cuota = (R * capital) / (1 - (1 + R) ** -N)
    return cuota, cuota * N 

capital = float(input("Introduce el capital del préstamo: "))
interes_anual = float(input("Introduce el interés anual (%): "))
años = int(input("Introduce el número de años del préstamo: "))

cuota_mensual, total_a_pagar = calcular_cuota_mensual(capital, interes_anual, años)

print(f"\nCuota mensual a pagar: {cuota_mensual:.2f} €")
print(f"Total a pagar al final del préstamo: {total_a_pagar:.2f} €")