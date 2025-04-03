from random import randint

# Programa que simula un pequeño juego de adivinación mental

# Incluimos un título
titulo = "juego de adivinación"
print(titulo.upper())
print("-" * len(titulo))

# Ronda de preguntas
primera_pregunta = int(input("¿Qué móvil crees que estoy usando?\n"
                             "[1] El último iPhone\n"
                             "[2] El mejor del momento\n"))
segunda_pregunta = int(input("¿En qué plato de comida crees que estoy pensando?\n"
                             "[1] Tortilla española\n"
                             "[2] Paella valenciana\n"
                             "[3] Asado Uruguayo\n"))
tercerapregunta = int(input("¿En qué numero del 1 al 10 estoy pensando?\n"))
numeroaleatorio = randint(1, 10)

# Resolvemos
if primera_pregunta == 2 and segunda_pregunta == 3 and tercerapregunta == numeroaleatorio:
    print("GUAUUUUUU. Eres un crack")
    print("Te tengo que fichar para mis inversiones en bolsa")
else:
    print("Lo se, un poco difícil, pero sigue jugando que seguro que lo consigues")
