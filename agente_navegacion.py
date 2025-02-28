from collections import deque
import time

# Laberinto: 0 = libre, 1 = pared, 'M' = meta
laberinto = [
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 'M']
]

# Movimiento: arriba, abajo, izquierda, derecha
movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

class Agente:
    def __init__(self, laberinto, inicio):
        self.laberinto = laberinto
        self.inicio = inicio
        self.filas = len(laberinto)
        self.columnas = len(laberinto[0])

    def es_valido(self, fila, col):
        """ Verifica si la posición es válida """
        return 0 <= fila < self.filas and 0 <= col < self.columnas and self.laberinto[fila][col] != 1

    def buscar_meta(self):
        """ Encuentra la ruta a la meta usando BFS """
        cola = deque([(self.inicio, [self.inicio])])
        visitados = {self.inicio}

        while cola:
            (fila, col), ruta = cola.popleft()

            # Si encontramos la meta, retornamos la ruta
            if self.laberinto[fila][col] == 'M':
                return ruta

            # Explorar los movimientos posibles
            for mov in movimientos:
                nf, nc = fila + mov[0], col + mov[1]
                if self.es_valido(nf, nc) and (nf, nc) not in visitados:
                    visitados.add((nf, nc))
                    cola.append(((nf, nc), ruta + [(nf, nc)]))
        
        return None  # Si no hay ruta

    def mostrar_ruta_consecutiva(self, ruta):
        """ Muestra la ruta del agente de manera consecutiva, paso a paso """
        for paso in ruta:
            print(f"Agente se mueve a: {paso}")
            self.mostrar_laberinto(paso)
            time.sleep(1)  # Pausa de 1 segundo para mostrar el movimiento de forma visual

    def mostrar_laberinto(self, paso):
        """ Muestra el laberinto con el agente en su posición actual """
        lab = [row[:] for row in self.laberinto]  # Copia del laberinto
        fila, col = paso
        lab[fila][col] = 'A'  # Marca la posición del agente

        for fila in lab:
            print(" ".join(str(celda) for celda in fila))
        print()

# Crear el agente con inicio en (0, 0)
agente = Agente(laberinto, (0, 0))

# Buscar la ruta hacia la meta y mostrarla paso a paso
ruta = agente.buscar_meta()
if ruta:
    print("Iniciando búsqueda de la salida...\n")
    agente.mostrar_ruta_consecutiva(ruta)
    print("¡Meta alcanzada!")
else:
    print("No se encontró una ruta.")
