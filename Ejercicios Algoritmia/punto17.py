"""
17.En Tecnólogo de ADSO del SENA hay 10 aprendices matriculados, pero un nuevo aprendiz se incorporará a formación. El listado de aprendices se encuentra ordenado alfabéticamente por
apellido. Ahora hay que incluir al nuevo aprendiz en la lista (mostrar la lista antes y después de ingresar al nuevo aprendiz).
"""
lista = ["Aguilar", "Barrios", "Castaño", "Delgado", "Escobar", 
         "González", "López", "Martínez", "Ramírez", "Zapata"]

print("Lista:", sorted(lista))

lista.append(input("Ingrese el apellido del nuevo aprendiz: "))
print("Lista actualizada:", sorted(lista))