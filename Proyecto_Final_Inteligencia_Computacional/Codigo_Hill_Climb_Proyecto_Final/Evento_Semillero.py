import random

# Datos de interés simulados (porcentajes de estudiantes interesados en cada tema)
intereses = {"Seguridad Informática": 63, "Tecnología": 76, "Auditoría": 29}

# Implementación del algoritmo de escalada (Hill Climb)
def hill_climb(intereses):
    # Elegimos un tema inicial aleatorio de la lista de temas disponibles
    tema_actual = random.choice(list(intereses.keys()))
    puntaje_actual = intereses[tema_actual]

    # Iteramos sobre los temas para encontrar el tema de máximo interés
    for tema, puntaje in intereses.items():
        # Comparación para verificar si encontramos un tema con mayor interés
        if puntaje > puntaje_actual:
            tema_actual = tema
            puntaje_actual = puntaje

    return tema_actual, puntaje_actual

# Ejecutamos el algoritmo
tema_maximo, puntaje_maximo = hill_climb(intereses)

# Mostramos el resultado
print(f"El tema de mayor interés es '{tema_maximo}' con un {puntaje_maximo}% de interés.")
