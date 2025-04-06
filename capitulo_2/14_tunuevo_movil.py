# Programa que ayuda a un usuario a elegir su nuevo móvil a través de
# una serie de preguntas

# Incluimos un título
titulo = "Tu selector de móvil"
print(titulo.upper())
print("-" * len(titulo))

# Primera pregunta sobre el tipo de SO
tipo_so = input("¿Qué tipo de SO quieres?\n"
                "[I]iOS\n"
                "[A]Android\n").upper()

# Comenzamos con el resto de preguntas dependiendo del SO
if tipo_so == "I":
    # comenzamos con el tipo iOS
    print("iOS")
    presupuesto = input("¿Cuánto te quieres gastar?\n"
                        "[N]No tengo problema\n"
                        "[S]Lo suficiente\n"
                        "[P]Poco\n").upper()
    modelo_nuevo = input("¿Quieres tener el último modelo?\n"
                         "[S]Por supuestísimo\n"
                         "[N]Me da lo mismo. Mientras sea de Apple\n").upper()
    # Árbol de decisiones iOS
    if presupuesto == "P" and modelo_nuevo == "S":
        print("Tu móvil ideal es: iPhone 16e")
        print("El precio es de: 709€")
    elif presupuesto == "P" and modelo_nuevo == "N":
        print("Tu móvil ideal es: iPhone 14")
        print("El precio es de: 599€")
    elif presupuesto == "S" and modelo_nuevo == "S":
        print("Tu móvil ideal es: iPhone 16")
        print("El precio es de: 959€")
    elif presupuesto == "S" and modelo_nuevo == "N":
        print("Tu móvil ideal es: iPhone 15 Pro")
        print("El precio es de: 1219€")
    elif presupuesto == "N" and modelo_nuevo == "S":
        print("Tu móvil ideal es: iPhone 16 Pro Max")
        print("El precio es de: 1479€")
    elif presupuesto == "N" and modelo_nuevo == "N":
        print("Tu móvil ideal es: iPhone 15 Pro Max")
        print("El precio es de: 1449€")
    else:
        print("Tu elección no corresponde a ninguna opción válida")

elif tipo_so == "A":
    # comenzamos con el tipo Android
    print("Android")
    tipo = input("¿Qué tipo de móvil buscas?\n"
                 "[A]Gama Alta\n"
                 "[M]Media\n"
                 "[B]Baja\n").upper()
    camara = input("¿Te importa la cámara?\n"
                   "[S]Por supuestísimo\n"
                   "[N]Me da lo mismo. Mientras pueda usar WhatsApp\n").upper()
    # Árbol de decisiones Android
    if tipo == "B" and camara == "S":
        print("Tu móvil ideal es: Redmi Note 14 Pro")
        print("El precio es de: 279€")
    elif tipo == "B" and camara == "N":
        print("Tu móvil ideal es: POCO M6 Pro")
        print("El precio es de: 260€")
    elif tipo == "M" and camara == "N":
        print("Tu móvil ideal es: Nothing Phone (3a)")
        print("El precio es de: 399€")
    elif tipo == "M" and camara == "S":
        print("Tu móvil ideal es: Pixel 9a")
        print("El precio es de: 529€")
    elif tipo == "A" and camara == "S":
        print("Tu móvil ideal es: Pixel 9 Pro")
        print("El precio es de: 1099€")
    elif tipo == "A" and camara == "N":
        print("Tu móvil ideal es: Samsung Galaxy S25 Ultra")
        print("El precio es de: 1459€")
    else:
        print("Tu elección no corresponde a ninguna opción válida")
else:
    # No se ha elegido correctamente
    print("Tu elección no corresponde a ninguna opción válida")