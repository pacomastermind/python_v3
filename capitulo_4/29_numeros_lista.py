# Ejemplo en el que se calcula el número máximo y número mínimo
# para una lista introducida por el usuario y separadas por coma

numero_introducidos = input("Introduzca los números separados por coma: ")  # 1,2,3,4,5,6
lista_de_numeros_de_usuario_string = numero_introducidos.split(",")
lista_de_numeros_de_usuario_int = [int(numero) for numero in lista_de_numeros_de_usuario_string]

print(lista_de_numeros_de_usuario_string)

#for numero in lista_de_numeros_de_usuario_string:
#    lista_de_numeros_de_usuario_int.append(int(numero))

# Comenzamos con la búsqueda del número más alto y más pequeño sin
# usar ni max ni min

numero_min = lista_de_numeros_de_usuario_int[0]
numero_max = lista_de_numeros_de_usuario_int[0]

for numero in lista_de_numeros_de_usuario_int[1:]:
    if numero_min > numero:
        numero_min = numero

    if numero_max < numero:
        numero_max = numero

print("Resultado final\n")
print(f"Numero más grande: {numero_max}\n"
      f"Numero más pequeño: {numero_min}")

print(lista_de_numeros_de_usuario_int)