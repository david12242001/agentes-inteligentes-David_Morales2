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
        print(f"El agente se detiene por un momento... \n")
        time.sleep(1)  # Hace que la simulación sea más lenta
        
        if self.detectar_obstaculo():
            print("¡Oh no! Un obstáculo ha sido detectado. El agente se detiene y piensa... ")
            time.sleep(1)  # Pausa más larga para simular que está pensando
            print("¡El agente decide cambiar de dirección! \n")
            self.cambiar_direccion()
        
        # Movimiento del agente
        self.posicion_actual += self.direccion
        
        # Mantener el agente dentro de los límites de la ruta
        if self.posicion_actual >= len(self.ruta):
            self.posicion_actual = len(self.ruta) - 1
            self.cambiar_direccion()
        elif self.posicion_actual < 0:
            self.posicion_actual = 0
            self.cambiar_direccion()
        
        # Simula el movimiento del agente de manera más humana
        print(f"El agente se mueve hacia: {self.ruta[self.posicion_actual]}")
        time.sleep(2)  # Pausa de 2 segundos para hacer el movimiento más lento

# Definir la ruta de patrullaje
ruta = ["A", "B", "C", "D", "E"]

# Crear el agente y simular su movimiento
agente = AgentePatrulla(ruta)

for _ in range(15):  # Simulación de 15 movimientos
    agente.mover()
