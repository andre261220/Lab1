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
