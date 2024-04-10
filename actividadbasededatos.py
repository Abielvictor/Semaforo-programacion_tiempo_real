# Función para establecer la conexión
# -*- coding: utf-8 -*-

import pyodbc

# Función para establecer la conexión


def establecer_conexion():
    server = 'LAPTOP-L76DLSJ9\SQLEXPRESS'
    database = 'EventosDB'

    conn_str = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + \
        server + ';DATABASE=' + database + ';Trusted_Connection=yes'

    try:
        conn = pyodbc.connect(conn_str)
        print("Conexión exitosa a la base de datos.")
        return conn
    except pyodbc.Error as ex:
        print("Error conectando la base de datos:", ex)
        return None

# Funciones de pruebas


def prueba_insercion_datos(conn):
    # Código para la prueba de inserción...
    pass


def prueba_consulta_datos(conn):
    # Código para la prueba de consulta...
    pass


def prueba_actualizacion_datos(conn):
    # Código para la prueba de actualización...
    pass


def prueba_eliminacion_datos(conn):
    # Código para la prueba de eliminación...
    pass

# Función para mostrar el menú y ejecutar la prueba seleccionada


def menu_principal(conn):
    while True:
        print("\nMENU PRINCIPAL")
        print("1. Prueba de Inserción de Datos")
        print("2. Prueba de Consulta de Datos")
        print("3. Prueba de Actualización de Datos")
        print("4. Prueba de Eliminación de Datos")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            prueba_insercion_datos(conn)
        elif opcion == '2':
            prueba_consulta_datos(conn)
        elif opcion == '3':
            prueba_actualizacion_datos(conn)
        elif opcion == '4':
            prueba_eliminacion_datos(conn)
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

# Programa principal


def main():
    # Establecer conexión
    conn = establecer_conexion()

    if conn is not None:
        # Mostrar el menú
        menu_principal(conn)

        # Cerrar la conexión
        conn.close()
    else:
        print("No se pudo establecer la conexión.")


if __name__ == "__main__":

    main()
