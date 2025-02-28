import random
import time

class AgentePatrulla:
    def __init__(self, ruta):
        self.ruta = ruta
        self.posicion_actual = 0
        self.direccion = 1  # 1 para adelante, -1 para atrás
    
    def detectar_obstaculo(self):
        # Simula la detección de un obstáculo en un 20% de los casos
        return random.random() < 0.2
    
    def cambiar_direccion(self):
        self.direccion *= -1
    
    def mover(self):
        if self.detectar_obstaculo():
            print("¡Obstáculo detectado! Cambiando dirección.")
            self.cambiar_direccion()
        
        self.posicion_actual += self.direccion
        
        # Mantener el agente dentro de los límites de la ruta
        if self.posicion_actual >= len(self.ruta):
            self.posicion_actual = len(self.ruta) - 1
            self.cambiar_direccion()
        elif self.posicion_actual < 0:
            self.posicion_actual = 0
            self.cambiar_direccion()
        
        print(f"Agente en posición: {self.ruta[self.posicion_actual]}")

# Definir la ruta de patrullaje
ruta = ["A", "B", "C", "D", "E"]

# Crear el agente y simular su movimiento
agente = AgentePatrulla(ruta)

for _ in range(15):  # Simulación de 15 movimientos
    agente.mover()
    time.sleep(1)
