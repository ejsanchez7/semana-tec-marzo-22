import random
import math

#Calcular el número
number = math.ceil((random.random() * 500)) + 1

print("\nBienvenido, el sistema 'pensará' un número entre 1 y 500 y deberás adivinarlo\n")

#Solicitar el número
guess = -1

while guess != number :

    guess = int(input("Introduce el número: "))

    if guess < number :

        print("Cerca! el número por adivinar es mayor.\n")

    elif guess > number :

        print("Cerca! el número por adivinar es menor.\n")

print(f"\nFelicidades! adivinaste el número '{number}'!\n")
