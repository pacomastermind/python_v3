# Programa que permite gestionar una lista de la compra
# con alimentos no repetidos

lista_de_la_compra = []
input_usuario = None  # None es un objeto en Python que significa que no tiene valor

titulo = "Programa lista de la compra"
print(titulo.upper())
print("-" * len(titulo))

# while input_usuario != "Q":
while True:
    input_usuario = input("¿Qué deseas comprar? ([Q] para salir): ").upper()
    # Comprobamos si la respuesta es Q
    if input_usuario == "Q":
        break
    # Comprobamos si esta en la lista
    if input_usuario in lista_de_la_compra:
        print(f"{input_usuario} ya está en la lista")
    else:
        confirmacion = input(f"¿Seguro que desea añadir {str(input_usuario)} a la lista de la compra? [S/N]").upper()
        if confirmacion == "S":
            # Añado a la lista
            lista_de_la_compra.append(input_usuario)
            print(f"{input_usuario} se añadió a la lista")

# Imprimimos la lista cuando salimos del while
print("La lista de la compra que necesitas es:")
print(lista_de_la_compra)
