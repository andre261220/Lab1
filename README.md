# Lab1
Reporte de la primer practica de Diseño de sistemas Robóticos -LRT4102-

## Intoducción a Python

Python es un lenguaje de programación de alto nivel, interpretado y multipropósito. Es conocido por su sintaxis clara y legible, lo que lo hace especialmente adecuado para principiantes y profesionales por igual. A continuación, se presenta una breve descripción de los conceptos básicos de Python:
1. Tipos de variables:
   
   * Números: enteros (int), decimales (float) y complejos (complex).
   * Cadenas de caracteres (str): secuencias de caracteres encerradas entre comillas simples o dobles.
   * Listas: secuencias ordenadas y mutables de elementos.
   * Tuplas: secuencias ordenadas e inmutables de elementos.
   * Diccionarios: colecciones no ordenadas de pares clave-valor.

3. Estructura de bucle *for*
El bucle *for* en Python se utiliza para iterar sobre una secuencia (como una lista, tupla, diccionario o cadena) o cualquier objeto iterable. La estructura general de un bucle *for* es la siguiente:

```python
   for elemento in secuencia:
    # Cuerpo del bucle
```

3.  Estructuras de un Bucle *while*

El bucle *while* en Python se utiliza para repetir un bloque de código mientras se cumpla una condición específica. La estructura general de un bucle *while* es la siguiente:

```python
    while condicion:
    # Cuerpo del bucle
```

4. Estructura de una declaracion *if-elif-else*
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

Deberá imprimir también la ruta que siguió.Mostrar un segundo mapa con el “camino” seguido por el robot mediante flechas


