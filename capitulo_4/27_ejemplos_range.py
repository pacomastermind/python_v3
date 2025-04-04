# Ejercicio con el que vamos a practicar range
#
# A partir del número introducido por el usuario
# debemos generar la tabla de multiplicar
# Ejemplo --> usuario introduce el 2
# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6
# 2 x 4 = 8
# 2 x 5 = 10
# 2 x 6 = 12
# 2 x 7 = 14
# 2 x 8 = 16
# 2 x 9 = 18
# 2 x 10 = 20

numero = int(input("Numero para generar la tabla de multiplicar: "))

for n in range(1,11):
    print(f"{numero} x {n} = {n * numero}")

print("------------------")

for n in range(1,11):
    if n%2 ==0:
        print(f"{numero} x {n} = {n * numero}")