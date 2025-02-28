import time
import random

# Definir el entorno como una matriz de celdas
mapa = [
    [0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

# Inicializar la posición del agente y la memoria de lugares visitados
posicion = (0, 0)
visitadas = set()

# Función para verificar si una posición es válida (dentro del mapa y libre de obstáculos)
def es_valida(pos):
    x, y = pos
    if 0 <= x < len(mapa) and 0 <= y < len(mapa[0]) and mapa[x][y] == 0:
        return True
    return False

# Función para explorar el mapa
def explorar():
    global posicion
    visitadas.add(posicion)  # Marca la posición inicial como visitada

    # Direcciones posibles de movimiento: arriba, abajo, izquierda, derecha
    direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    print(f"Agente comienza en: {posicion}")
    time.sleep(1)

    while len(visitadas) < len(mapa) * len(mapa[0]):
        posibles_movimientos = []

        # Generar los posibles movimientos
        for dx, dy in direcciones:
            nueva_pos = (posicion[0] + dx, posicion[1] + dy)
            if es_valida(nueva_pos) and nueva_pos not in visitadas:
                posibles_movimientos.append(nueva_pos)
        
        if posibles_movimientos:
            # Elegir un movimiento aleatorio de los posibles
            posicion = random.choice(posibles_movimientos)
            visitadas.add(posicion)
            print(f"\nExplorando: {posicion}...")
            time.sleep(random.uniform(0.5, 1.5))  # Hacer la simulación más lenta y natural
            
            # Simular reacción del agente
            print(f"¡Nuevo descubrimiento! El agente está explorando una zona desconocida.")
            time.sleep(1)
        else:
            # Si no hay más celdas por explorar, el agente termina la exploración
            print("\n¡No hay más áreas por explorar! El agente ha explorado todo lo posible.")
            break

# Llamar a la función de exploración
explorar()
