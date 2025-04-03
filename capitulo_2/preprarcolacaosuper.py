# Programa para preparar un ColaCao
print("Voy hacia la cocina")

# Comprobamos si hay leche y colacao
print("Abro la nevera")
hay_leche = input("¿Hay leche en la nevera? [S/N]")
print("Abro la despensa")
hay_colacao = input("¿Hay ColaCao en la despensa? [S/N]")
hay_galletas = input("¿Hay Galletas en la despensa? [S/N]")

# Una vez que he comprobado, si falta cualquier ingrediente tengo
# que ir al super
if hay_colacao != "S" or hay_leche != "S" or hay_galletas != "S":
    print("Tengo que ir al super. Me falta algún ingrediente")
    # Me falta leche
    if hay_leche != "S":
        print("Tengo que comprar leche. Lo anoto en la lista")
    # Me falta leche
    if hay_colacao != "S":
        print("Tengo que comprar colacao. Lo anoto en la lista")

# SI hay colacao. Y también leche. Porque si no había he ido al super
print("Tengo leche y tengo Colacao")
print("Mezclo la leche con el Colacao")
print("Me TOMO mi Colacao")
