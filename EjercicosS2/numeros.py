# Definir una lista de números
numeros = [5, 15, 18, 12, 7, 6, 31, 69, 50, 11]

# Inicializar variables para calcular el promedio de números pares y el producto de números impares
suma_pares = 0
cantidad_pares = 0
producto_impares = 1

# Iterar sobre la lista de números
for numero in numeros:
    if numero % 2 == 0:  # Verificar si el número es par
        suma_pares += numero
        cantidad_pares += 1
    else:  # Si el número es impar
        producto_impares *= numero

# Calcular el promedio de números pares
if cantidad_pares > 0:
    promedio_pares = suma_pares / cantidad_pares
else:
    promedio_pares = 0

# Imprimir resultados
print(f"El promedio de los números pares es: {promedio_pares}")
print(f"El producto de los números impares es: {producto_impares}")
