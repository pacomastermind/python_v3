# Programa para preparar un ColaCao
print("Voy hacia la cocina")

# El primer paso será comprobar si hay leche
print("Abro la nevera")
hayleche = input("¿Hay leche en la nevera? [S/N]")

# Punto de control. ¿Hay leche?
if hayleche == "S":
    # SI hay leche
    print("Hay leche en la nevera")
    #Segundo punto de control. ¿Hay colacao?
    print("Abro la despensa")
    haycolacao = input("¿Hay ColaCao en la despensa? [S/N]")
    if haycolacao == "S":
        # SI hay colacao. Y también leche
        print("Hay colacao en la despensa")
        print("Mezclo la leche con el Colacao")
        print("Me TOMO mi Colacao")

# Fin de programa
print("Fin de programa")