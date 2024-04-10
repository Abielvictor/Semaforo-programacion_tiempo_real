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

semaphore = threading.Semaphore(1)

stop_event = threading.Event()

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

        with open("estados_semaforo.txt", "w") as file:
            file.write("\n".join(semaforo_estados))
            file.write("\n")
            file.close()
    except Exception as e:
        print(f"Error en la conexión: {e}")
    finally:
        conexion.close()


sem_thread = threading.Thread(target=semaforo)
sem_thread.start()

while True:
    try:
        conexion, addr = my_socket.accept()
        threading.Thread(target=handle_connection,
                         args=(conexion, addr)).start()
    except Exception as e:
        print(f"Error al aceptar conexión: {e}")

stop_event.set()
my_socket.close()
