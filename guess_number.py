import random
import math

#Límite de intentos
triesLimit = 10
tries = 0

#Calcular el número
number = math.ceil((random.random() * 1000)) + 1

print("\nBienvenido, el sistema 'calculará' un número entre 1 y 1000 y deberás adivinarlo\n")

#Solicitar el número
guess = -1

while guess != number and tries < triesLimit :

    guess = int(input("Introduce el número: "))
    tries += 1

    if guess < number :

        print("Cerca! el número por adivinar es mayor.\n")

    elif guess > number :

        print("Cerca! el número por adivinar es menor.\n")

    print(f"Intentos disponibles: {triesLimit - tries}\n")

if tries == triesLimit:
    print("Has alcanzado el número permitido de intentos, suerte para la próxima!\n")
else:
    print(f"\nFelicidades! adivinaste el número '{number}'!\n")
