import threading
import time

# Definimos un semáforo para controlar el acceso a la impresora

semaphore = threading.Semaphore(1)

# Función que simula imprimir un documento


def imprimir(documento, id_proceso):
    print(f"Proceso {id_proceso}: imprimiendo {documento}")
    time.sleep(2)  # Simulamos el tiempo que toma imprimir
    print(f"Proceso {id_proceso}: documento {documento} impreso")

# Función que simula el trabajo de un proceso


def proceso(documento, id_proceso):
    global semaphore
    semaphore.acquire()  # Adquirimos el semáforo para la ejecucion
    imprimir(documento, id_proceso)
    semaphore.release()  # Liberamos el semáforo

# Creamos algunos procesos que intentarán imprimir documentos


procesos = []
for i in range(1, 6):
    documento = f"Documento_{i}"
    proceso_thread = threading.Thread(target=proceso, args=(documento, i))
    procesos.append(proceso_thread)

# Iniciamos los procesos

for proceso_thread in procesos:
    proceso_thread.start()

# Esperamos a que todos los procesos terminen

for proceso_thread in procesos:
    proceso_thread.join()

print("Todos los procesos han terminado.")
