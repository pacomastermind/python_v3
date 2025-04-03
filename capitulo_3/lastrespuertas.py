#Primer programa con while para ver su uso


# contador = 0
# print("Entramos en el while")
# while contador < 10:
#     print(contador)
#     contador = contador + 1
# print("Hemos salido del while")

puerta = input("Te encuentras ante el reto final de la aventura\n"
               "Delante de tí 3 puertas, con inscripciones en nórdico\n\n"
               "La primera puerta marca ODIN\n"
               "La segunda puerta pone FREYA\n"
               "La tercera puerta indica LOKI\n\n"
               "... Y en el suelo unas runas con el símbolo de la belleza.\n"
               "¿Qué puerta eliges?[ODIN|FREYA|LOKI]?\n").upper()

while( puerta != "ODIN" and puerta != "FREYA" and puerta != "LOKI"):
    #No se ha elegido ninguna de las tres opciones
    #volvemos a preguntar
    puerta = input ("Te has equivocado en tu decisión\n"
                    "Tienes que elegir una de las tres puertas\n"
                    "ODIN, FREYA o LOKI\n").upper()

#Si llegamos aquí la elección ha sido correcta
if puerta == "ODIN" :
    print("\nEl Dios de la guerra\n"
          "Mala elección\n"
          "Te regala una coraza y te da una espada y te castiga a luchar contra los elfos oscuros\n"
          "por el resto de la eternidad\n")
elif puerta == "FREYA" :
    print("\nLa Diosa de la belleza, perfecto!\n"
          "Conoces a los dioses\n"
          "Te estaba esperando, te regala una vida próspera y te deja marchar en libertad\n")
elif puerta == "LOKI" :
    print("\nEl Dios del enagaño!\n"
          "La peor puerta que podrías haber elegido\n"
          "Intercambias el sitio en el que estaba Loki, atado a tres rocas, dejando en libertad a Loki\n"
          "y tu esclavizado por el resto de tus días\n")