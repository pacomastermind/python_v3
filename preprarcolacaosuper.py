# Programa para preparar un ColaCao
print("Voy hacia la cocina")

# Comprobamos si hay leche y colacao
print("Abro la nevera")
hayleche = input("¿Hay leche en la nevera? [S/N]")
print("Abro la despensa")
haycolacao = input("¿Hay ColaCao en la despensa? [S/N]")
haygalletas = input("¿Hay Galletas en la despensa? [S/N]")


# Una vez que he comprobado, si falta cualquier ingrediente tengo
# que ir al super
if haycolacao != "S" or hayleche != "S" or haygalletas!= "S":
    print("Tengo que ir al super. Me falta algún ingrediente")
    # Me falta leche
    if hayleche != "S":
        print("Tengo que comprar leche. Lo anoto en la lista")
    # Me falta leche
    if haycolacao != "S":
        print("Tengo que comprar colacao. Lo anoto en la lista")

# SI hay colacao. Y también leche. Porque si no había he ido al super
print("Tengo leche y tengo Colacao")
print("Mezclo la leche con el Colacao")
print("Me TOMO mi Colacao")