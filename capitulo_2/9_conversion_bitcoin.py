# Conversor de bitcoins
# Pedimos al usuario cuantos bitcoins tiene en su monedero
bitcoins = float(input("¿Cuantos bitcoins tienes?"))
euro_bitcoin = 80524.11
euros = bitcoins * euro_bitcoin
print(f"El número de bitcoins que tienes: {bitcoins}")
# Formateamos la salida con solo dos valores decimales
print(f"El dinero en euros es de: {euros:.2f}€")
# Nos quedamos con la parte entera
euros_int = int(euros)
print(f"El dinero en euros es de: {euros_int}€")