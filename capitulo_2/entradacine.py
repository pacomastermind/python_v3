# Programa que nos permite calcular el precio final de la entrada de cine
# aplicando descuentos necesarios

# Comenzamos creando las variables necesarias para calcular el descuento
descuento_edad = 0
descuento_carnet = 0
descuento_final = 0

# Incluimos un título
titulo = "Venta de entradas cine"
print(titulo.upper())
print("-" * len(titulo))

# Preguntamos al cliente
edad = int(input("¿Qué edad tienes?\n"))
tipocarnet = input("¿Qué tipo de carnet tienes?\n"
                   "[E]Estudiante\n"
                   "[F]Familia Numerosa\n"
                   "[P]Pensionista\n"
                   "[N]Ninguno\n").upper()

# Calculamos el primer descuento a partir de la edad
if edad < 10 or edad > 70:
    # Se aplica el descuento del 10%
    descuento_edad = 10

# Calculamos el segundo descuento el de carnet
if tipocarnet != "N":
    if tipocarnet == "E":
        # Se aplica el descuento del 5%
        descuento_carnet = 5
    if tipocarnet == "F":
        # Se aplica el descuento del 20%
        descuento_carnet = 20
    if tipocarnet == "P":
        # Se aplica el descuento del 30%
        descuento_carnet = 30

# Calculamos el descuento final
if descuento_edad > descuento_carnet:
    descuento_final = descuento_edad
else:
    descuento_final = descuento_carnet

# Calculamos el precio final de la entrada y mostramos por pantalla
precio_entrada = 6
preciocon_descuento = precio_entrada - ((descuento_final / 100) * precio_entrada)

print("-" * len(titulo))
print(f"Tu entrada cuesta {preciocon_descuento:.2f}€")
print(f"Se ha aplicado un descuento final del {descuento_final}% sobre {precio_entrada}€")
