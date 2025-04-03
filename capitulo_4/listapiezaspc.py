# Programa que almacena todas las piezas del PC que necesito construir

# lista vacia de piezas
lista_piezas = []

pieza = input("¿Cuál es la pieza que vas a necesitar? Escribe FIN para terminar")
while pieza != "FIN":
    lista_piezas.append(pieza)
    pieza = input("¿Quieres añadir otra pieza? Escribe FIN para terminar")
