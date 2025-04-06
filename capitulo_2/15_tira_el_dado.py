"""
from random import randint

# Generamos un número aleatorio entre 1 y 6
numero = randint(1, 6)

print("He lanzado un dado...")
print(f"El número que ha salido es: {numero}")



Ejercicio para los alumnos
"""

from random import randint

# Tirar el dado
numero = randint(1, 6)

# Mostrar el resultado
print(f"Ha salido el número: {numero}")
print()

# Mostrar el dibujo correspondiente
if numero == 1:
    print("+-------+")
    print("|       |")
    print("|   o   |")
    print("|       |")
    print("+-------+")
elif numero == 2:
    print("+-------+")
    print("| o     |")
    print("|       |")
    print("|     o |")
    print("+-------+")
elif numero == 3:
    print("+-------+")
    print("| o     |")
    print("|   o   |")
    print("|     o |")
    print("+-------+")
elif numero == 4:
    print("+-------+")
    print("| o   o |")
    print("|       |")
    print("| o   o |")
    print("+-------+")
elif numero == 5:
    print("+-------+")
    print("| o   o |")
    print("|   o   |")
    print("| o   o |")
    print("+-------+")
elif numero == 6:
    print("+-------+")
    print("| o   o |")
    print("| o   o |")
    print("| o   o |")
    print("+-------+")