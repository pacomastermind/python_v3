#Batalla Pokémon
from random import randint

#Constante que configura el número de estrellas a mostrar
NUM_ASTERISCOS = 20
#Variables que controlan la vida de cada Pokémon
VIDAINICIAL_PIKACHU = 100
VIDAINICIAL_SQUIRTLE = 100
vida_pikachu = VIDAINICIAL_PIKACHU
vida_squirtle = VIDAINICIAL_SQUIRTLE

turno = 0

#Comienza la batalla
while vida_pikachu > 0 and vida_squirtle > 0:
    turno += 1
    print(f"-------- TURNO {turno} --------")
    #Comienza el turno Pikachu
    #De forma aleatoria elegirá entre dos ataques
    ataque_pikachu = randint(1,2)

    if ataque_pikachu == 1:
        #Bola Voltio
        print("Pikachu ataca con Bola Voltio")
        #vida_squirtle = vida_squirtle - 20
        vida_squirtle -= 20
    elif ataque_pikachu == 2:
        #Onda Trueno
        print("Pikachu ataca con Onda TRueno")
        vida_squirtle -= 30

    #Fin turno Pikachu
    #Mostramos las vidas
    barravida_pikachu = int(vida_pikachu * NUM_ASTERISCOS / VIDAINICIAL_PIKACHU)
    barravida_squirtle = int(vida_squirtle * NUM_ASTERISCOS / VIDAINICIAL_SQUIRTLE)
    print(f"\nLa vida de Pikachu es [{vida_pikachu}/{VIDAINICIAL_PIKACHU}] [{"*"*barravida_pikachu}]")
    print(f"La vida de Squirtle es [{vida_squirtle}/{VIDAINICIAL_SQUIRTLE}] [{"*"*barravida_squirtle}]")
    #Comprobamos que la vida de Squirtle es mayor a 0
    #Si no lo es finalizamos nuestro programa
    if vida_squirtle <= 0:
        break
    # Comienza el turno Squirtle
    ataque_squirtle = input("¿Qué ataque deseas realizar? [P]lacaje o Pistola de [A]gua").upper()
    while ataque_squirtle != "P" and ataque_squirtle != "A":
        ataque_squirtle = input("¿Qué ataque deseas realizar? [P]lacaje o Pistola de [A]gua").upper()

    if ataque_squirtle == "P":
        #Bola Voltio
        print("Squirtle ataca con Placaje")
        vida_pikachu -= 10
    elif ataque_squirtle == "A":
        #Pistola de Agua
        print("Squirtle ataca con Pistola de Agua")
        vida_pikachu -= 40

    # Fin turno Squirtle
    # Fin TURNOS
    #Mostramos las vidas
    barravida_pikachu = int(vida_pikachu * NUM_ASTERISCOS / VIDAINICIAL_PIKACHU)
    barravida_squirtle = int(vida_squirtle * NUM_ASTERISCOS / VIDAINICIAL_SQUIRTLE)
    print(f"\nLa vida de Pikachu es [{vida_pikachu}/{VIDAINICIAL_PIKACHU}] [{"*"*barravida_pikachu}]")
    print(f"La vida de Squirtle es [{vida_squirtle}/{VIDAINICIAL_SQUIRTLE}] [{"*"*barravida_squirtle}]")

#SALIMOS DEL WHILE
#COMPROBAMOS QUIEN GANA
if vida_pikachu > vida_squirtle:
    print("Ha ganado Pikachu")
else:
    print("Ha ganado Squirtle")