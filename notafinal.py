# Pedimos las tres notas al usuario
nota1 = int(input("Escribe tu primera nota: "))
nota2 = int(input("Escribe tu segunda nota: "))
nota3 = int(input("Escribe tu tercera nota: "))
# Hacemos el cálculo
notafinal = (nota1 + nota2 + nota3) / 3
notamax = max(nota1, nota2, nota3)
notamin = min(nota1, nota2, nota3)
# Imprimimos resultado
print(f"La nota final que has conseguido es {notafinal}")
print(f"La nota más alta conseguida entre {nota1},{nota2} y {nota3} es {notamax}")
print(f"La nota más baja conseguida entre {nota1},{nota2} y {nota3} es {notamin}")