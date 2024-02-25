# Lab1
Reporte de la primer practica de Diseño de sistemas Robóticos -LRT4102-

## Introducción a Python

Python es un lenguaje de programación de alto nivel, interpretado y multipropósito. Es conocido por su sintaxis clara y legible, lo que lo hace especialmente adecuado para principiantes y profesionales por igual. A continuación, se presenta una breve descripción de los conceptos básicos de Python:
1. Tipos de variables:
   
   * Números: enteros (int), decimales (float) y complejos (complex).
   * Cadenas de caracteres (str): secuencias de caracteres encerradas entre comillas simples o dobles.
   * Listas: secuencias ordenadas y mutables de elementos.
   * Tuplas: secuencias ordenadas e inmutables de elementos.
   * Diccionarios: colecciones no ordenadas de pares clave-valor.

2. Estructura de bucle *for*:
   
El bucle *for* en Python se utiliza para iterar sobre una secuencia (como una lista, tupla, diccionario o cadena) o cualquier objeto iterable. La estructura general de un bucle *for* es la siguiente:

```python
   for elemento in secuencia:
    # Cuerpo del bucle
```

3.  Estructuras de un Bucle *while*:

El bucle *while* en Python se utiliza para repetir un bloque de código mientras se cumpla una condición específica. La estructura general de un bucle *while* es la siguiente:

```python
    while condicion:
    # Cuerpo del bucle
```

4. Estructura de una declaracion *if-elif-else*:

La declaración *if* se utiliza para ejecutar un bloque de código si se cumple una condición específica. La estructura general de una declaración *if* es la siguiente:

```python
if condicion:
    # Cuerpo del bloque if
elif otra_condicion:
    # Cuerpo del bloque elif
else:
    # Cuerpo del bloque else (opcional)
```

5. Funciones:

Las funciones en Python son bloques de código reutilizables que realizan una tarea específica. Se definen utilizando la palabra clave *def*. La estructura general de una función es la siguiente:

```python
    def nombre_funcion(parametros):
    # Cuerpo de la función
    return resultado
```

Estos son algunos de los conceptos básicos de Python que se explicaron en clase de laboratorio de Diseño de Sistemas, estos nos dan una base sólida para comenzar a programar en este lenguaje. Python es versátil y cuenta con una amplia gama de bibliotecas, de las cuales se nos dio una breve explicación de igual manera en clase usando como ejemplo la libreria random en un ejercicio, asi como tambien cuenta con herramientas que lo hacen útil en una variedad de campos, como desarrollo web, análisis de datos, inteligencia artificial y más.

## Problemas a Resolver

1. Escribir un programa que lea un entero positivo “n” introducido por el usuario y después muestreen pantalla la suma de todos los enteros desde 1 hasta n . La suma de los primeros enterospositivos puede ser calculada de la siguiente forma:
   
   ![suma](https://github.com/andre261220/Lab1/assets/132303647/9d4b63ea-3d91-49ce-9749-6a20d85a2a8d)
   
2. Escribir un programa que pregunte al usuario por el número de horas trabajadas y el costo por hora.Después debe mostrar por pantalla la paga que le corresponde.
3. Crear una lista de nombre + sueldo por hora + horas trabajadas de al menos seis operadores.Imprime el nombre y el sueldo a pagar de cada operador.
4. Crear una lista llamada numeros que contenga al menos 10 números, calcula el promedio de los números pares y el producto de los números impares eI imprime los resultados.
5. Crear un programa que solicite al usuario adivinar un número secreto. El programa debe generarun número aleatorio entre 1 y 10, y el usuario debe intentar adivinarlo. El programa debeproporcionar pistas si el número ingresado por el usuario es demasiado alto o bajo. El bucle whiledebe continuar hasta que el usuario adivine correctamente. Al final se debe imprimir en cuantosintentos el usuario logró adivinar el número.
6. **Robot explorador:**
   
El programa debe generar una matriz de al menos 5x5. El robot inicia su camino en la posición (0,0) de la matriz y debe salir en la posición (4,4) o lamáxima posición si se cambia el tamaño de matriz. El numero y la posición de los obstáculos es aleatoria.El robot solo puede avanzar, girar a la izquierda o a la derecha para buscar un camino libre, en eleventual caso que el robot no pueda salir debe imprimir en pantalla “Imposible llegar al destino”En caso de que el robot llegue a su destino final deberá imprimir el mapa, con los espacios libres yobstáculos de la siguiente forma X obstáculo o libre.

o o X o o

o o o o o

o o o o X

o o o o o

o X X X o

Deberá imprimir también la ruta que siguió. Mostrar un segundo mapa con el “camino” seguido por el robot mediante flechas.

##Solucion de los problemas

1. **suma.py**

```python
n = int(input("inntoduce un numero entero: "))
suma = n*(n+1)/2
print ("la suma de tu numero entero es: " + str(suma))
```

Este programa calcula la suma de los primeros `n` números enteros. A continuación, se describe la solución paso a paso:

El programa solicita al usuario que introduzca un número entero utilizando la función `input()`. El valor ingresado por el usuario se convierte a entero utilizando `int()` y se almacena en la variable `n`.

Luego, calcula la suma de los primeros `n` números enteros utilizando la fórmula matemática de la suma de una serie aritmética: `suma = n*(n+1)/2`. Esta fórmula se basa en el principio de que la suma de los números de 1 a `n` es igual a `(n*(n+1))/2`.

Finalmente, imprime el resultado de la suma utilizando la función `print()`. El resultado se convierte a cadena utilizando `str()` para poder concatenarlo con el mensaje de texto.
En resumen, este programa toma un número entero ingresado por el usuario, calcula la suma de los primeros `n` números enteros y luego imprime el resultado.

***Ejemplo de resultado del programa***
```
inntoduce un numero entero: 2
la suma de tu numero entero es: 3.0
```

2. **trabajo.py**

```python
h = int(input("Introduce el número de horas trabajadas: "))
c = int(input( "Introduce el costo por hora: " + "$"))
p = h * c
print("Su pago correpondiente es: " + "$"+ str(p)) 
```

Este programa calcula el pago correspondiente a un trabajador en función del número de horas trabajadas y el costo por hora. Aquí está la descripción de la solución:

El programa solicita al usuario que introduzca el número de horas trabajadas utilizando la función `input()`. El valor ingresado por el usuario se convierte a entero utilizando `int()` y se almacena en la variable `h`.

Luego, solicita al usuario que introduzca el costo por hora utilizando la función `input()`. El valor ingresado por el usuario se convierte a entero utilizando `int()` y se almacena en la variable `c`.

El programa calcula el pago correspondiente multiplicando el número de horas trabajadas (`h`) por el costo por hora (`c`) y almacena el resultado en la variable `p`.

Finalmente, el programa imprime el resultado utilizando la función `print()`. El resultado se convierte a cadena utilizando `str()` para poder concatenarlo con el mensaje de texto que indica el pago correspondiente. La cadena resultante se concatena con el símbolo "$" para denotar que se trata de una cantidad de dinero.

***Ejemplo de resultado del programa***
```
Introduce el número de horas trabajadas: 2
Introduce el costo por hora: $500
Su pago correpondiente es: $1000
```

3.  **lista.py**

```python
# Definir una lista de operadores con sus respectivos datos
operadores = [
    {"nombre": "Jesus", "sueldo_por_hora": 10, "horas_trabajadas": 40},
    {"nombre": "Andre", "sueldo_por_hora": 12, "horas_trabajadas": 35},
    {"nombre": "Nacho", "sueldo_por_hora": 9, "horas_trabajadas": 45},
    {"nombre": "Charvel", "sueldo_por_hora": 11, "horas_trabajadas": 38},
    {"nombre": "Enrique", "sueldo_por_hora": 10, "horas_trabajadas": 42},
    {"nombre": "Aldo", "sueldo_por_hora": 13, "horas_trabajadas": 37}
]

# Función para calcular el sueldo a pagar por operador
def calcular_sueldo(nombre, sueldo_por_hora, horas_trabajadas):
    sueldo = sueldo_por_hora * horas_trabajadas
    return sueldo

# Imprimir el nombre y el sueldo a pagar de cada operador
for operador in operadores:
    nombre = operador["nombre"]
    sueldo_por_hora = operador["sueldo_por_hora"]
    horas_trabajadas = operador["horas_trabajadas"]
    sueldo_a_pagar = calcular_sueldo(nombre, sueldo_por_hora, horas_trabajadas)
    print(f"El operador {nombre} debe recibir un sueldo de ${sueldo_a_pagar}.")
```

Este programa crea una lista de operadores con sus respectivos nombres, sueldos por hora y horas trabajadas. Luego, utiliza una función para calcular el sueldo a pagar por cada operador multiplicando el sueldo por hora por las horas trabajadas. Finalmente, imprime el nombre de cada operador junto con el sueldo que debe recibir.

***Ejemplo de resultado del programa***
```
El operador Jesus debe recibir un sueldo de $400.
El operador Andre debe recibir un sueldo de $420.
El operador Nacho debe recibir un sueldo de $405.
El operador Charvel debe recibir un sueldo de $418.
El operador Enrique debe recibir un sueldo de $420.
El operador Aldo debe recibir un sueldo de $481.
```

4. **numeros.py**

```python
# Definir una lista de números
numeros = [5, 15, 8, 12, 7, 6, 31, 69, 50, 11]

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
```

Este programa crea una lista llamada numeros que contiene al menos 10 números. Luego, itera sobre esta lista y calcula la suma de los números pares y el producto de los números impares. Finalmente, calcula el promedio de los números pares (si hay números pares en la lista) y los imprime junto con el producto de los números impares.

***Ejemplo de resultado del programa***
```
El promedio de los números pares es: 21.5
El producto de los números impares es: 12352725
```

5. **NoSecreto.py**

```python
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
```

Este programa genera un número aleatorio entre 1 y 10 y luego solicita al usuario que adivine el número. Proporciona pistas si el número ingresado es demasiado alto o bajo. El bucle while continuará hasta que el usuario adivine correctamente el número secreto. Una vez que el usuario adivina correctamente, el programa imprime cuántos intentos le tomó al usuario adivinar el número.

***Ejemplo de resultado del programa***
```
Adivina el número secreto (entre 1 y 10): 4
El número es demasiado bajo. Inténtalo de nuevo.
Adivina el número secreto (entre 1 y 10): 8
¡Felicidades! ¡Adivinaste el número secreto!
Número de intentos: 2
```

6. **Robot Explorador**
Descripcion del ultimo problema que se podra encontrar en la carpeta EjerciciosS2.

**Importación de bibliotecas:**
   - `import random`: Importa el módulo `random`, que se utiliza para generar números aleatorios.
   - `import numpy as np`: Importa el módulo `numpy` bajo el alias `np`, que se utiliza para trabajar con matrices de manera eficiente.

**Creación de la matriz:**
   - Se define el tamaño de la matriz como `size = 5`.
   - Se crea una matriz de tamaño `(size, size)` con todos los elementos inicializados con `'o'` utilizando `np.full()`.

**Colocación de obstáculos aleatorios:**
   - Utilizando un bucle `for`, se seleccionan aleatoriamente las posiciones `(i, j)` dentro de la matriz y se asigna el valor `'X'` a esas posiciones para representar los obstáculos.

**Definición de la posición inicial y final del robot:**
   - `start = (0, 0)`: Define la posición inicial del robot en la esquina superior izquierda de la matriz.
   - `end = (size-1, size-1)`: Define la posición final del robot en la esquina inferior derecha de la matriz.

**Función para encontrar el camino:**
   - `find_path(matrix, start, end)`: Define una función llamada `find_path` que toma la matriz, la posición inicial y la posición final del robot como argumentos.
   - La función utiliza una búsqueda en profundidad (DFS) para encontrar un camino desde la posición inicial hasta la posición final, evitando los obstáculos.
   - Utiliza una pila (`stack`) para realizar la búsqueda.
   - Devuelve el camino encontrado si existe, o `None` si no se puede encontrar un camino.

**Encontrar el camino:**
   - Se llama a la función `find_path` con la matriz, la posición inicial y final del robot.
   - El resultado se almacena en la variable `path`.

**Imprimir el resultado:**
   - Si no se encuentra un camino (`path is None`), imprime "Imposible llegar al destino".
   - Si se encuentra un camino, imprime el mapa original y el camino seguido.
   - En el mapa original, los obstáculos están representados por 'X'.
   - En el camino seguido, las flechas indican la dirección que tomó el robot para alcanzar el destino. Las flechas son: '→' (derecha), '↓' (abajo), '←' (izquierda) y '↑' (arriba).

Este programa utiliza un enfoque de búsqueda en profundidad para encontrar un camino desde la posición inicial hasta la posición final en una matriz con obstáculos aleatorios. Luego, imprime tanto el mapa original como el camino seguido por el robot.

***Ejemplo de resultado del programa***
```
Mapa original:
o o o X o
o o o o o
X o o X o
o o o o o
o X X o o
Camino seguido:
o ↑ → X o
↓ → ↓ o o
X ← ↓ X o
o ↓ → → o
o X X ↓ →
```


