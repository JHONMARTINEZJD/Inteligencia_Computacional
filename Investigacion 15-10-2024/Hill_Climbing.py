import random

# Definimos un conjunto de programas con sus costos y distancias
programas = {
    "Ingeniería de Software": {"costo": 3000, "distancia": 10},
    "Ingeniería Civil": {"costo": 3500, "distancia": 5},
    "Medicina": {"costo": 5000, "distancia": 15},
    "Derecho": {"costo": 2500, "distancia": 20},
    "Arquitectura": {"costo": 2800, "distancia": 8},
}

# Función de evaluación que intenta minimizar la distancia y el costo
def evaluar(programa):
    return programa["costo"] + programa["distancia"]

# Función Hill Climbing
def hill_climbing(programas):
    # Seleccionar un programa inicial aleatoriamente
    solucion_actual = random.choice(list(programas.keys()))
    print(f"Solución inicial: {solucion_actual}")

    while True:
        # Encontrar los vecinos (programas disponibles)
        vecinos = list(programas.keys())
        vecinos.remove(solucion_actual)

        # Evaluar la solución actual
        mejor_vecino = solucion_actual
        mejor_valor = evaluar(programas[solucion_actual])

        # Comparar con los vecinos
        for vecino in vecinos:
            valor_vecino = evaluar(programas[vecino])
            if valor_vecino < mejor_valor:
                mejor_vecino = vecino
                mejor_valor = valor_vecino

        # Si no se encuentra un vecino mejor, terminar
        if mejor_vecino == solucion_actual:
            break

        # Moverse al mejor vecino
        solucion_actual = mejor_vecino
        print(f"Mejor vecino: {solucion_actual}")

    return solucion_actual

# Ejecutamos el algoritmo
mejor_programa = hill_climbing(programas)
print(f"El mejor programa es: {mejor_programa}")
