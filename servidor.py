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


def semaforo():
    global semaphore
    while True:
        with semaphore:
            print("Verde")
            time.sleep(1)

            print("Amarillo")
            time.sleep(1)

            print("Rojo")
            time.sleep(3)
        # Llamada recursiva para mantener el ciclo del semáforo
        semaforo()


def handle_connection(conexion, addr):
    print('Conectado')
    print(addr)

    request = conexion.recv(1024)
    print(request)

    # Se ejecuta la función semaforo para controlar el acceso
    semaforo()

    conexion.close()


while True:
    conexion, addr = my_socket.accept()

    # Creamos un hilo para manejar cada conexión

    threading.Thread(target=handle_connection, args=(conexion, addr)).start()
