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
    gasto = input("¿Cuanto te quieres gastar?\n"
                  "[N]No tengo problema\n"
                  "[S]Suficiente\n"
                  "[P]Poco\n").upper()
    modelo = input("¿Quieres tener el último modelo?\n"
                   "[S]Por supuestísimo\n"
                   "[N]Me da lo mismo. Mientras sea un Apple\n").upper()
    # Montamos el arbol de decisiones
    if gasto == "P":
        print("Tu móvil ideal es: iPhone 16e")
        print("El precio es de: 709€")
    elif gasto == "S" and modelo == "S":
        print("Tu móvil ideal es: iPhone 16")
        print("El precio es de: 959€")
    elif gasto == "S" and modelo == "N":
        print("Tu móvil ideal es: iPhone 15")
        print("El precio es de: 859€")
    elif gasto == "N" and modelo == "S":
        print("Tu móvil ideal es: iPhone 16 Pro Max")
        print("El precio es de: 1219€")
    elif gasto == "N" and modelo == "N":
        print("Tu móvil ideal es: iPhone 15 Plus")
        print("El precio es de: 959€")
    else:
        print("Tu ejección no corresponde a ninguna opción válida")
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
    # Montamos el arbol de decisiones
    if tipo == "A" and camara == "S":
        print("Tu móvil ideal es: Xiaomi 15 Ultra")
        print("El precio es de: 1021€")
    elif tipo == "M" and camara == "S":
        print("Tu móvil ideal es: Pixel 7a")
        print("El precio es de: 448€")
    elif tipo == "B" and camara == "S":
        print("Tu móvil ideal es: Redmi Note 12")
        print("El precio es de: 249€")
    elif tipo == "A" and camara == "N":
        print("Tu móvil ideal es: Samsung Galaxy S25")
        print("El precio es de: 1459€")
    elif tipo == "A" and camara == "N":
        print("Tu móvil ideal es: Redmi Note 13 Pro+")
        print("El precio es de: 430€")
    elif tipo == "A" and camara == "N":
        print("Tu móvil ideal es: POCO M6 Pro")
        print("El precio es de: 260€")
    else:
        print("Tu ejección no corresponde a ninguna opción válida")
else:
    # No se ha elegido correctamente no podemos ayudar
    print("Tu ejección no corresponde a ninguna opción válida")
