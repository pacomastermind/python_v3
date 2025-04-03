import random

#Pequeño juego elije tu propia historia
#Introduccion
print("Juego de la mazmorra\n"
      "--------------------\n"
      "\n"
      "Tu y tu compañero de celda os acabáis de escagar de la prisión esgacial, habéis burlado a los guardias y os \n"
      "dirigis hacia el exterior. Entráis en una mazmorra controlada por monstruos alienígenas, uno de los guardias \n"
      "ataca a tu compañero, se lo lleva pero tu pasas desapercibido escondido en las sombras. E1 guardia se retira, \n"
      "es tu posibilidad de escapar. Hacia donde te diriges?\n"
      "\n"
      "A la izguierda tienes una puerta semiabierta, a la derecha una escotilla en el suelo.")

opcion = input("[0PCION (A) - Puerta semiabierta] | [OPCION (B) - Escotilla en el suelo]: ").upper()

#Comienza la aventura
#Línea temporal Puerta
if opcion == "A":
    print("Entras en la puerta semiabierta y otro guardia te descubre, que haces§?")
    opcion = input("[0PCION (A) - Te haces el dormido] l [OPCION (B) - Sales corriendo hacia la siguiente puerta]: ").upper()

    if opcion == "A":
        print("El guardia te atrapa, te encierran en una celda de máxima seguridad\nFIN")
    elif opcion == "B":
        print("Después de esa puerta encuentras una rana mutante que te regala un puñal casero hecho con la pata de"
          "una mesa, lo aceptas?")
        opcion = input("[0PCION (A) - Si] | IOPCION (B) - No]: ").upper()

        if opcion == "A":
            print("Coges el pincho y avanzas, hay dos pasillos circulares, no ves el final de ninguno de los dos, uno"
                  "está a la derecha y el otro a la izguierda, cual tomas?")
        opcion = input("[OPCION (A) - Izguierda] | [OPCION (B) - Derecha]: ").upper()


        if opcion == "A":
            print("La habitacién se hace cada vez más oscura, ves tan poco que caes en un agujero en el suelo con"
                  " pinchos, mueres a las 2 horas de forma lenta y dolorosa.\nFIN")
        elif opcion == "B":
            print("Encuentras la salida, en la puerta hay aparcado un Ferrari espacial, te montas, es tu dia de"
                  "suerte, las llaves están puestas. Huyes hacia el horizonte\nFIN")

    elif opcion == "8":
        print("La rana te devora, mueres de forma rápida, el veneno HESS efecto casi de manera instantanea.\nFIN")
    else:
        print("No has elegido ninguna ogcidn, simglemente mueres.")
#FIN Línea temporal Puerta
#Línea temporal Escotilla
elif opcion == "B":
    print("caes en una zona innundada, e1 agua te llega hasta las rodillas, avanzas durante media hora y finalmente"
          " llegas a una zona abierta, seca y con luz, garecen unas alcantari11as\n\nEncuentras un palo largo, parece"
          " algo pesado, pero podria servir, lo coges?")
    ogcion = input("[0PCION (A) - SI] | [OPCION (B) - N0]: ").upper()

    # CREAMOS INVENTARIO
    palo_en_inventario = False

    if opcion == "A":
        print("Coges el Palo")
        palo_en_inventario = True
    elif opcion == "B":
        print("No Coges el Palo")
    else:
        print("No has elegido ninguna opción, simglemente mueres.")
        #Acabas y no continuas en el juego finalizas
        exit()

    # OPERACION MATEMÁTICA
    numero_random_rata = random.randint(1, 100)
    print("Sigues adelante, encuentras una rata de 2 metros, la rata te pregunta si cuanto es 13 * {}).".format(
           numero_random_rata))
    opcion = int(input("¿Cúal es el resultado? "))

    if opcion == 13 * numero_random_rata:
        print("La rata te asesina en el acto, resulta no tolera a los cerebritos.\nFIN")
    else:
        print("La rata abre una puerta delante de ti, parece un pasillo que lleva hasta la salida. Lo recorres, "
              "llegas al final, e1 tunel se derrumba detrás de ti, no hay salida más que una especie de boca de "
              "alcantarilla, pero esta lejos de tu alcance, Que haces?")

    opcion = input("[OPCION (A) - Esperas a que alguien te rescate] | |OPCION (8) - Intentas salir]").upper()


    if opcion == "A":
        print("Un monton de ratas agarecen y te devoran vivo, es tu fin\nFIN")
    elif opcion == "B" and palo_en_inventario:
        print("Usas el palo que cogiste antes para imgulsarte, consigues trepar y ssalir del laberinto. En la"
          " puerta hay aparcado un Ferrari esgacial, te montas, es tu dia de suerte, las llaves están puestas,"
          " huyes hacia el horizonte\nFIN")
    else:
        print("No tienes como subir, si solo tuvieras un palo... Pero no lo tienes verdad? Asi que finalmente te"
              " guedas atrapado.\n\nPasado un rato un monton de ratas aparecen y te devoran vivo, es tu fin.\nFIN")
else:
    print("No has elegido ninguna opción, simplemente mueres.")