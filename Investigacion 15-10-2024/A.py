import heapq

# Definimos un conjunto de programas con costo, distancia y calidad
programas = {
    "Ingeniería de Software": {"costo": 3000, "distancia": 10, "calidad": 8},
    "Ingeniería Civil": {"costo": 3500, "distancia": 5, "calidad": 7},
    "Medicina": {"costo": 5000, "distancia": 15, "calidad": 9},
    "Derecho": {"costo": 2500, "distancia": 20, "calidad": 6},
    "Arquitectura": {"costo": 2800, "distancia": 8, "calidad": 8},
}

# Heurística: tratar de minimizar el costo y la distancia
def heuristica(programa):
    return programa["distancia"] * 2 - programa["calidad"] * 10

# Función de evaluación que suma el costo y la heurística
def evaluar_a_estrella(programa):
    return programa["costo"] + heuristica(programa)

# Algoritmo A*
def a_estrella(programas):
    # Utilizamos una cola de prioridad (heap)
    pq = []
    for nombre, datos in programas.items():
        # La prioridad es el valor calculado con la heurística y costo
        valor = evaluar_a_estrella(datos)
        heapq.heappush(pq, (valor, nombre))

    # Obtenemos el mejor programa
    mejor_valor, mejor_programa = heapq.heappop(pq)
    print(f"El mejor programa es: {mejor_programa} con valor: {mejor_valor}")
    return mejor_programa

# Ejecutamos el algoritmo
mejor_programa_a_estrella = a_estrella(programas)
