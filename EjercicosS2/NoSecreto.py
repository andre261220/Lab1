import random

# Generar un número aleatorio entre 1 y 10
numero_secreto = random.randint(1, 10)

intentos = 0
adivinado = False

# Bucle while para continuar hasta que el usuario adivine el número
while not adivinado:
    # Solicitar al usuario que ingrese un número
    intento = int(input("Adivina el número secreto (entre 1 y 10): "))
    intentos += 1
    
    # Comprobar si el número ingresado es igual al número secreto
    if intento == numero_secreto:
        print("¡Felicidades! ¡Adivinaste el número secreto!")
        print("Número de intentos:", intentos)
        adivinado = True
    # Proporcionar pistas si el número es demasiado alto o bajo
    elif intento < numero_secreto:
        print("El número es demasiado bajo. Inténtalo de nuevo.")
    else:
        print("El número es demasiado alto. Inténtalo de nuevo.")
