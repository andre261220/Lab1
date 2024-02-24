import random

# Función para crear la matriz con obstáculos aleatorios
def crear_matriz(n):
    matriz = [['o' for _ in range(n)] for _ in range(n)]
    for _ in range(n):  # Agregar obstáculos aleatorios
        fila = random.randint(0, n - 1)
        columna = random.randint(0, n - 1)
        matriz[fila][columna] = 'X'
    return matriz

# Función para imprimir la matriz
def imprimir_matriz(matriz):
    for fila in matriz:
        print(" ".join(fila))

# Función para verificar si la posición está dentro de la matriz
def dentro_de_matriz(posicion, n):
    x, y = posicion
    return 0 <= x < n and 0 <= y < n

# Función para mover el robot
def mover_robot(matriz, ruta, posicion, direccion):
    direcciones = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Derecha, Abajo, Izquierda, Arriba
    x, y = posicion
    for _ in range(4):  # Realizar un ciclo completo buscando un camino libre
        dx, dy = direcciones[direccion]
        nueva_posicion = (x + dx, y + dy)
        if dentro_de_matriz(nueva_posicion, len(matriz)) and matriz[nueva_posicion[0]][nueva_posicion[1]] == 'o':
            ruta.append((nueva_posicion, direccion))
            return nueva_posicion, direccion
        direccion = (direccion + 1) % 4
    return None, None  # No hay camino libre en ninguna dirección

# Tamaño de la matriz
n = 5
# Crear la matriz con obstáculos aleatorios
matriz = crear_matriz(n)
# Posición inicial del robot
posicion_actual = (0, 0)
# Dirección inicial del robot (hacia la derecha)
direccion_actual = 0
# Ruta seguida por el robot
ruta = [(posicion_actual, direccion_actual)]

# Mover el robot hasta llegar al destino o determinar que es imposible llegar
while posicion_actual != (n - 1, n - 1):
    posicion_actual, direccion_actual = mover_robot(matriz, ruta, posicion_actual, direccion_actual)
    if posicion_actual is None:
        print("Imposible llegar al destino.")
        break

# Si el robot llega al destino final
if posicion_actual == (n - 1, n - 1):
    print("El robot llegó al destino final:")
    # Imprimir la matriz con el camino seguido
    for paso, _ in ruta:
        x, y = paso
        matriz[x][y] = '→'
    imprimir_matriz(matriz)

    # Imprimir la ruta seguida por el robot
    print("\nRuta seguida por el robot:")
    for paso, direccion in ruta:
        x, y = paso
        if direccion == 0:
            matriz[x][y] = '→'
        elif direccion == 1:
            matriz[x][y] = '↓'
        elif direccion == 2:
            matriz[x][y] = '←'
        elif direccion == 3:
            matriz[x][y] = '↑'
    imprimir_matriz(matriz)
