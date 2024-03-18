import threading
import time

# Número total de asientos disponibles
NUM_ASIENTOS = 10

# Lista de asientos disponibles
asientos_disponibles = list(range(1, NUM_ASIENTOS + 1))

# Función para reservar un asiento


def reservar_asiento(cliente):
    global asientos_disponibles
    if asientos_disponibles:
        # Simulando un tiempo de procesamiento
        time.sleep(1)
        # Reservar el primer asiento disponible
        asiento = asientos_disponibles.pop(0)
        print(f"Cliente {cliente} reservó el asiento {asiento}")
    else:
        print(f"Cliente {cliente} no pudo reservar un asiento. Teatro lleno.")

# Simulación de múltiples clientes intentando reservar asientos


def main():
    # Crear 5 hilos (clientes)
    hilos = []
    for i in range(1, 6):
        hilo = threading.Thread(target=reservar_asiento, args=(i,))
        hilos.append(hilo)
        hilo.start()

    # Esperar a que todos los hilos terminen
    for hilo in hilos:
        hilo.join()


if __name__ == "__main__":
    main()
