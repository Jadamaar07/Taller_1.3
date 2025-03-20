import os
def limpiar_terminal():
    os.system("CLS")
limpiar_terminal()
globals().clear()

vocales = ["a","e","i","o","u","A","E","I","O","U"]

letra = input("Ingrese la letra: ")

if letra in vocales:
    print("La letra es una vocal ")

else:
    print("La letra no es una vocal")