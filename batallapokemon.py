#Batalla Pokémon
from random import randint

#Constante que configura el número de estrellas a mostrar
NUM_ASTERISCOS = 20
#Variables que controlan la vida de cada Pokémon
VIDAINICIAL_PIKACHU = 100
VIDAINICIAL_SQUIRTLE = 100
vidapikachu = VIDAINICIAL_PIKACHU
vidasquirtle = VIDAINICIAL_SQUIRTLE

turno = 0

#Comienza la batalla
while vidapikachu > 0 and vidasquirtle > 0:
    turno += 1
    print(f"-------- TURNO {turno} --------")
    #Comienza el turno Pikachu
    #De forma aleatoria elegirá entre dos ataques
    ataquepikachu = randint(1,2)

    if ataquepikachu == 1:
        #Bola Voltio
        print("Pikachu ataca con Bola Voltio")
        #vidasquirtle = vidasquirtle - 20
        vidasquirtle -= 20
    elif ataquepikachu == 2:
        #Onda Trueno
        print("Pikachu ataca con Onda TRueno")
        vidasquirtle -= 30

    #Fin turno Pikachu
    #Mostramos las vidas
    barravidapikachu = int(vidapikachu * NUM_ASTERISCOS / VIDAINICIAL_PIKACHU)
    barravidasquirtle = int(vidasquirtle * NUM_ASTERISCOS / VIDAINICIAL_SQUIRTLE)
    print(f"\nLa vida de Pikachu es [{vidapikachu}/{VIDAINICIAL_PIKACHU}] [{"*"*barravidapikachu}]")
    print(f"La vida de Squirtle es [{vidasquirtle}/{VIDAINICIAL_SQUIRTLE}] [{"*"*barravidasquirtle}]")
    #Comprobamos que la vida de Squirtle es mayor a 0
    #Si no lo es finalizamos nuestro programa
    if vidasquirtle <= 0:
        break
    # Comienza el turno Squirtle
    ataqueaquirtle = input("¿Qué ataque deseas realizar? [P]lacaje o Pistola de [A]gua").upper()
    while ataqueaquirtle != "P" and ataqueaquirtle != "A":
        ataqueaquirtle = input("¿Qué ataque deseas realizar? [P]lacaje o Pistola de [A]gua").upper()

    if ataqueaquirtle == "P":
        #Bola Voltio
        print("Squirtle ataca con Placaje")
        vidapikachu -= 10
    elif ataqueaquirtle == "A":
        #Pistola de Agua
        print("Squirtle ataca con Pistola de Agua")
        vidapikachu -= 40

    # Fin turno Squirtle
    # Fin TURNOS
    #Mostramos las vidas
    barravidapikachu = int(vidapikachu * NUM_ASTERISCOS / VIDAINICIAL_PIKACHU)
    barravidasquirtle = int(vidasquirtle * NUM_ASTERISCOS / VIDAINICIAL_SQUIRTLE)
    print(f"\nLa vida de Pikachu es [{vidapikachu}/{VIDAINICIAL_PIKACHU}] [{"*"*barravidapikachu}]")
    print(f"La vida de Squirtle es [{vidasquirtle}/{VIDAINICIAL_SQUIRTLE}] [{"*"*barravidasquirtle}]")

#SALIMOS DEL WHILE
#COMPROBAMOS QUIEN GANA
if vidapikachu > vidasquirtle:
    print("Ha ganado Pikachu")
else:
    print("Ha ganado Squirtle")