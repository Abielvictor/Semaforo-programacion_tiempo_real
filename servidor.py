import socket
import time

my_socket = socket.socket()
my_socket.bind(('localhost', 8000))
my_socket.listen(5)


def semaforo():
    while True:
        print("verde")
        time.sleep(1)

        print("Amarillo")
        time.sleep(1)

        print("Rojo")
        time.sleep(1)


while True:
    conexion, addr = my_socket.accept()
    print('connected')
    print(addr)

    request = conexion.recv(1024)
    print(request)

    semaforo()
    conexion.close()
