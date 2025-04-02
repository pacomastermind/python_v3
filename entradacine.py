#Programa que nos permite calcular el precio final de la entrada de cine
#aplicando descuentos necesarios

#Comenzamos creando las variables necesarias para calcular el descuento
descuentoedad = 0
descuentocarnet = 0
descuentofinal = 0

#Incluimos un título
titulo = "Venta de entradas cine"
print(titulo.upper())
print("-"*len(titulo))

#Preguntamos al cliente
edad = int(input("¿Qué edad tienes?\n"))
tipocarnet = input( "¿Qué tipo de carnet tienes?\n"
                    "[E]Estudiante\n"
                    "[F]Familia Numerosa\n"
                    "[P]Pensionista\n"
                    "[N]Ninguno\n").upper()

#Calculamos el primer descuento a partir de la edad
if (edad<10 or edad>70):
    #Se aplica el descuento del 10%
    descuentoedad = 10

#Calculamos el segundo descuento el de carnet
if (tipocarnet != "N"):
    if(tipocarnet == "E"):
        # Se aplica el descuento del 5%
        descuentocarnet = 5
    if(tipocarnet == "F"):
        # Se aplica el descuento del 20%
        descuentocarnet = 20
    if(tipocarnet == "P"):
        # Se aplica el descuento del 30%
        descuentocarnet = 30

#Calculamos el descuento final
if (descuentoedad>descuentocarnet):
    descuentofinal = descuentoedad
else:
    descuentofinal = descuentocarnet

#Calculamos el precio final de la entrada y mostramos por pantalla
precioentrada=6
preciocondescuento=precioentrada-((descuentofinal/100)*precioentrada)

print("-"*len(titulo))
print(f"Tu entrada cuesta {preciocondescuento:.2f}€")
print(f"Se ha aplicado un descuento final del {descuentofinal}% sobre {precioentrada}€")