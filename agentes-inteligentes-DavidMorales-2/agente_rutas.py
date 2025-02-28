import random

# Representamos el entorno con una matriz de recompensas
# Cada número en la matriz representa la recompensa en esa celda
entorno = [
    [1, 4, 3, 2],
    [2, 1, 5, 1],
    [3, 2, 4, 6],
    [1, 3, 2, 8]
]

# Dirección de movimiento: [arriba, abajo, izquierda, derecha]
movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Función para mostrar el entorno de manera más comprensible
def mostrar_entorno():
    print("Entorno con valores de recompensa:")
    for fila in entorno:
        print(fila)
    print()

# Función para calcular la utilidad del camino: suma de las recompensas de cada celda
def utilidad(camino):
    return sum(entorno[x][y] for x, y in camino)

# Función para encontrar el mejor camino con la mayor utilidad desde el inicio hasta el fin
def seleccionar_ruta(inicio, fin):
    fila, col = inicio
    camino = [inicio]
    
    print(f"Buscando el camino más rentable desde {inicio} hasta {fin}...\n")

    while (fila, col) != fin:
        posibles_movimientos = []
        
        # Evaluar los posibles movimientos en cada dirección (arriba, abajo, izquierda, derecha)
        for dx, dy in movimientos:
            nueva_fila, nueva_col = fila + dx, col + dy
            
            # Verificar que el movimiento no salga del entorno
            if 0 <= nueva_fila < len(entorno) and 0 <= nueva_col < len(entorno[0]):
                posibles_movimientos.append((nueva_fila, nueva_col))
        
        # Escoger el movimiento con la mayor recompensa (utilidad)
        fila, col = max(posibles_movimientos, key=lambda x: entorno[x[0]][x[1]])
        camino.append((fila, col))
        
        # Mostrar el movimiento del agente en cada paso
        print(f"Agente se mueve a: ({fila}, {col}) - Recompensa en esta celda: {entorno[fila][col]}")
    
    return camino

# Función para mostrar el recorrido detallado del agente
def mostrar_recorrido(camino):
    print("\nRecorrido completo del agente:")
    for i, (x, y) in enumerate(camino):
        print(f"Paso {i + 1}: Celda ({x}, {y}) - Recompensa: {entorno[x][y]}")
    
# Inicio y fin del agente (posición de inicio y meta)
inicio = (0, 0)
fin = (3, 3)

# Mostrar el entorno inicial
mostrar_entorno()

# Encontrar la ruta óptima con la función de selección de rutas
camino_optimo = seleccionar_ruta(inicio, fin)

# Mostrar el recorrido final
mostrar_recorrido(camino_optimo)

# Mostrar la utilidad total del camino
print(f"\nUtilidad total del camino: {utilidad(camino_optimo)}")
