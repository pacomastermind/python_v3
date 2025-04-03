# Programa en el que inicializamos una nueva lista de vocales
# para realizar operaciones básicas
lista_letras = ["a", "b", "c", "d", "e"]
print(lista_letras[0])  # imprimiria la a
print(lista_letras[2])  # imprimiria la c
#print(lista_letras[5])  # error
print(len(lista_letras))
lista_letras.append("f") # acabo de añadir una nueva letra
print(lista_letras[5])  # No da error
print(len(lista_letras))
print(lista_letras)
lista_letras.pop()
print(lista_letras) # Hemos eliminado la última letra en este caso la f
lista_letras.pop(1)
print(lista_letras) # Hemos eliminado la última letra en este caso la f
print(lista_letras[1]) #imprime c

#Comprobar que una letra está dentro de la lista
letra_w = "w"
letra_a = "a"

print(letra_a in lista_letras) # Devolverá True
print(letra_w in lista_letras) # Devolverá False
