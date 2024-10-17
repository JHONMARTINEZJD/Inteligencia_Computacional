import heapq

# Agregamos un criterio de calidad a los programas
programas = {
    "Ingeniería de Software": {"costo": 3000, "distancia": 10, "calidad": 8},
    "Ingeniería Civil": {"costo": 3500, "distancia": 5, "calidad": 7},
    "Medicina": {"costo": 5000, "distancia": 15, "calidad": 9},
    "Derecho": {"costo": 2500, "distancia": 20, "calidad": 6},
    "Arquitectura": {"costo": 2800, "distancia": 8, "calidad": 8},
}

# Evaluación considerando costo, distancia y calidad (minimizamos costo y distancia, maximizamos calidad)
def evaluar(programa):
    return programa["costo"] + programa["distancia"] - programa["calidad"] * 100

# Función Beam Search
def beam_search(programas, ancho_beam):
    candidatos = list(programas.keys())
    mejor_soluciones = [(evaluar(programas[p]), p) for p in candidatos]
    heapq.heapify(mejor_soluciones)

    # Mantener solo los mejores 'ancho_beam' programas
    mejores = heapq.nsmallest(ancho_beam, mejor_soluciones)
    
    # Mostrar los candidatos seleccionados en cada paso
    for valor, programa in mejores:
        print(f"Programa: {programa}, Valor: {valor}")
    
    return [p for v, p in mejores]

# Ejecutamos el algoritmo con un ancho de beam de 2
mejores_programas = beam_search(programas, 2)
print(f"Los mejores programas son: {mejores_programas}")
