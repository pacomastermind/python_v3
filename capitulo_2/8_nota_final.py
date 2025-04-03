# Pedimos las tres notas al usuario
nota1 = int(input("Escribe tu primera nota: "))
nota2 = int(input("Escribe tu segunda nota: "))
nota3 = int(input("Escribe tu tercera nota: "))
# Hacemos el cálculo
nota_final = (nota1 + nota2 + nota3) / 3
nota_max = max(nota1, nota2, nota3)
nota_min = min(nota1, nota2, nota3)
# Imprimimos resultado
print(f"La nota final que has conseguido es {nota_final}")
print(f"La nota más alta conseguida entre {nota1},{nota2} y {nota3} es {nota_max}")
print(f"La nota más baja conseguida entre {nota1},{nota2} y {nota3} es {nota_min}")
