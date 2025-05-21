import random
tam = 10
matriz = [[random.randint(10, 99) for i in range (tam)] for j in range(tam)]
print ("\n-------- MATRIZ ---------")
for fila in matriz:
    print(fila)

print ("\n-------- DIAGONAL MATRIZ --------")
for i in range(tam):
    print(f"[{"    "*i}{matriz[i][i]}{"    "*(tam-i-1)}]")

print ("\n-------- DIAGONAL INVERSA --------")
for i in range(tam):
    print(f"[{'    '*(tam-i-1)}{matriz[i][tam-i-1]}{'    '*i }]")

print ()

print ("\n-------- MATRIZ INFERIOR IZQUIERDA ---------")
for i in range(tam):
    print("[", end="  ")
    for j in range(i+1):
        print(f"{matriz[i][j]}, ", end="")

    print('    ' * (tam -i),']')
print()

print ("\n-------- MATRIZ SUPERIOR IZQUIERDA ---------")
for i in range(tam):
    print("[", end="  ")
    for j in range(tam - i):
        print(matriz[i][j], end=" ")

    print('   ' * i,']')
print()

print ("\n-------- MATRIZ SUPERIOR DERECHA ---------")
for i in range(tam):

    print("["+"    " * i, end="") 
    for j in range (i, tam):
        print(f"{matriz[i][j]}, ", end="")
    print(']')

print()

print ("\n-------- MATRIZ INFERIOR IZQUIERDA ---------")
for i in range(tam):

    print("["+"    " * (tam -1 -i), end="") 
    for i in range (tam - i, tam):
        print(f"{matriz[i][j]}, ", end="")
    print('' * i,']')

print()