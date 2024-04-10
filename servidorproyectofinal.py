# import socket
# import time

# my_socket = socket.socket()
# my_socket.bind(('localhost', 8000))
# my_socket.listen(5)


# def semaforo():
# while True:
#  print("verde")
#   time.sleep(1)

#    print("Amarillo")
#     time.sleep(1)

#      print("Rojo")
#       time.sleep(1)


# while True:
# conexion, addr = my_socket.accept()
# print('connected')
# print(addr)

# request = conexion.recv(1024)
# print(request)

#  semaforo()
#   conexion.close()

import socket
import threading
import time

my_socket = socket.socket()
my_socket.bind(('localhost', 8000))
my_socket.listen(5)

# Creamos un semáforo con un valor inicial de 1
semaphore = threading.Semaphore(1)

# Creamos un evento para señalizar cuando se debe detener el semáforo
stop_event = threading.Event()

# Lista para almacenar los estados del semáforo
semaforo_estados = []


def semaforo():
    global semaphore, stop_event, semaforo_estados
    try:
        while not stop_event.is_set():
            with semaphore:
                semaforo_estados.append("Verde")
                time.sleep(1)

                semaforo_estados.append("Amarillo")
                time.sleep(1)

                semaforo_estados.append("Rojo")
                time.sleep(3)
    except Exception as e:
        print(f"Error en el semáforo: {e}")


def handle_connection(conexion, addr):
    global semaforo_estados
    print('Conectado')
    print(addr)

    try:
        request = conexion.recv(1024)
        print(request)
        conexion.send(b'Semaforo inteligente - Respuesta')

        # Guardar los estados del semáforo en un archivo txt
        with open("estados_semaforo.txt", "w") as file:
            file.write("\n".join(semaforo_estados))
            file.write("\n")
            file.close()
    except Exception as e:
        print(f"Error en la conexión: {e}")
    finally:
        conexion.close()


# Creamos un hilo para el semáforo
sem_thread = threading.Thread(target=semaforo)
sem_thread.start()

while True:
    try:
        conexion, addr = my_socket.accept()
        # Creamos un hilo para manejar cada conexión
        threading.Thread(target=handle_connection,
                         args=(conexion, addr)).start()
    except Exception as e:
        print(f"Error al aceptar conexión: {e}")

# Evento para detener el semáforo cuando se cierre el socket
stop_event.set()
my_socket.close()
