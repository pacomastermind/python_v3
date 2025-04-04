# En este ejercicio vamos a contabilizar los
# puntos
# comas
# espacios en blanco
import string

num_espacios = 0
num_comas = 0
num_puntos = 0
num_mayusculas = 0
num_minusculas = 0

abecedario_sp = string.ascii_lowercase + "ñ"
# print (abecedario_sp)

frase = input("Introduzca un texto a analizar: \n")

# Bucle de análisis de la frase
for letra in frase:
    # Bloque de signos de puntuación
    if letra == " ":
        num_espacios += 1
    elif letra == ",":
        num_comas += 1
    elif letra == '.':
        num_puntos += 1
    elif letra in abecedario_sp:
        num_minusculas += 1
    elif letra in abecedario_sp.upper():
        num_mayusculas += 1

# Imprimimos el resultado
print("El resultado del análisis de la frase ha sido:")
print(f"Espacios: {num_espacios}\n"
      f"Puntos: {num_puntos}\n"
      f"Comas: {num_comas}\n"
      f"Mayúsculas: {num_mayusculas}\n"
      f"Minúsculas: {num_minusculas}\n")
