# En este fichero realizaremos diversos ejemplos con el bucle for
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for item in lista_numeros:
    print(item)

# Ejemplo con lista de la compra
lista_de_la_compra = ["leche", "arroz", "jamon"]

for item in lista_de_la_compra:
    print(f"Voy a comprar {item}")

# Ejemplo de objeto interable con un string
frase = "Hola, hoy estoy aprendiendo python"

for letra in frase:
    print(letra.upper())

# Ejemplo cuenta vocales
vocales = ["a", "e", "i", "o", "u"]
cuenta_vocales = 0

for letra in frase:
    if letra in vocales:
        print(f"He encontrado la vocal {letra}")
        cuenta_vocales += 1

print(f"Hemos encontrado {cuenta_vocales} vocales dentro de la frase")

# Repetir n veces dentro del for

for i in [0, 1, 2]:
    print("WARNING!")

for i in range(3):
    print("WARNING!")

for i in range(1, 11):
    print(f"WARNING {i}!")

for i in range(10, 0, -1):
    print(f"Despegue en {i}!")
