# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 10:01:05 2023

@author: Erick
"""
from admins import Admin
from clientes import Cliente
from usuarios import Usuario


# def gestionar_usuarios():
#     while True:
#         print("\n--- Gestionar usuarios ---")
#         print("1. Cargar XML de usuarios")
#         print("2. Crear usuarios")
#         print("3. Modificar usuarios")
#         print("4. Eliminar usuarios")
#         print("5. Regresar al menú anterior")
#         opcion = input("Ingrese una opción: ")

#         if opcion == "1":
#             # Lógica para cargar XML de usuarios
#             print("Cargando XML de usuarios...")
#         elif opcion == "2":
#             # Lógica para crear usuarios
#             print("Creando usuarios...")
#         elif opcion == "3":
#             # Lógica para modificar usuarios
#             print("Modificando usuarios...")
#         elif opcion == "4":
#             # Lógica para eliminar usuarios
#             print("Eliminando usuarios...")
#         elif opcion == "5":
#             break
#         else:
#             print("Opción inválida. Por favor, elija nuevamente.")


# def gestionar_categorias_peliculas():
#     while True:
#         print("\n--- Gestionar categorías y películas ---")
#         print("1. Cargar XML de categorías y películas")
#         print("2. Crear categorías y películas")
#         print("3. Modificar categorías y películas")
#         print("4. Eliminar categoría y películas")
#         print("5. Regresar al menú anterior")
#         opcion = input("Ingrese una opción: ")

#         if opcion == "1":
#             # Lógica para cargar XML de categorías y películas
#             print("Cargando XML de categorías y películas...")
#         elif opcion == "2":
#             # Lógica para crear categorías y películas
#             print("Creando categorías y películas...")
#         elif opcion == "3":
#             # Lógica para modificar categorías y películas
#             print("Modificando categorías y películas...")
#         elif opcion == "4":
#             # Lógica para eliminar categoría y películas
#             print("Eliminando categoría y películas...")
#         elif opcion == "5":
#             break
#         else:
#             print("Opción inválida. Por favor, elija nuevamente.")


# def gestionar_salas():
#     while True:
#         print("\n--- Gestionar salas ---")
#         print("1. Cargar XML de salas")
#         print("2. Crear salas")
#         print("3. Modificar salas")
#         print("4. Eliminar salas")
#         print("5. Regresar al menú anterior")
#         opcion = input("Ingrese una opción: ")

#         if opcion == "1":
#             # Lógica para cargar XML de salas
#             print("Cargando XML de salas...")
#         elif opcion == "2":
#             # Lógica para crear salas
#             print("Creando salas...")
#         elif opcion == "3":
#             # Lógica para modificar salas
#             print("Modificando salas...")
#         elif opcion == "4":
#             # Lógica para eliminar salas
#             print("Eliminando salas...")
#         elif opcion == "5":
#             break
#         else:
#             print("Opción inválida. Por favor, elija nuevamente.")


def iniciar_sesion_administrador():
    correo = input("Ingrese su correo electrónico: ")
    contrasena = input("Ingrese su contraseña: ")
    Admin.iniciar_sesion_admin(correo, contrasena)
    
    # while True:
    #     print("\n--- Administrador ---")
    #     print("1. Gestionar usuarios")
    #     print("2. Gestionar categorías y películas")
    #     print("3. Gestionar salas")
    #     print("4. Cerrar sesión")
    #     opcion = input("Ingrese una opción: ")

        # if opcion == "1":
        #     gestionar_usuarios()
        # elif opcion == "2":
        #     gestionar_categorias_peliculas()
        # elif opcion == "3":
        #     gestionar_salas()
        # elif opcion == "4":
        #     break
        # else:
        #     print("Opción inválida. Por favor, elija nuevamente.")
            
def iniciar_sesion_cliente():
    correo = input("Ingrese su correo electrónico: ")
    contrasena = input("Ingrese su contraseña: ")
    Cliente.iniciar_sesion(correo, contrasena)
    # while True:
    #     print("\n--- Cliente ---")
    #     print("1. Ver listado de películas")
    #     print("2. Listado de películas favoritas")
    #     print("3. Comprar boletos")
    #     print("4. Historial de boletos comprados")
    #     print("5. Cerrar sesión")
    #     opcion = input("Ingrese una opción: ")

    #     if opcion == "1":
    #         # Lógica para ver listado de películas
    #         print("Mostrando listado de películas...")
    #     elif opcion == "2":
    #         # Lógica para ver listado de películas favoritas
    #         print("Mostrando listado de películas favoritas...")
    #     elif opcion == "3":
    #         # Lógica para comprar boletos
    #         print("Comprando boletos...")
    #     elif opcion == "4":
    #         # Lógica para ver historial de boletos comprados
    #         print("Mostrando historial de boletos comprados...")
    #     elif opcion == "5":
    #         break
    #     else:
    #         print("Opción inválida. Por favor, elija nuevamente.")
            
def mostrar_menu():
    while True:
        print("\n--- Menú ---")
        print("1. Iniciar sesión")
        print("2. Registrar usuario")
        print("3. Ver listado de películas")
        print("4. Salir del programa")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            print("\n--- Iniciar sesión ---")
            print("1. Administrador")
            print("2. Cliente")
            print("3. Regresar al menú anterior")
            tipo_usuario = input("Ingrese el tipo de usuario: ")
    
            if tipo_usuario == "1":
                iniciar_sesion_administrador()
            elif tipo_usuario == "2":
                iniciar_sesion_cliente()
            elif tipo_usuario == "3":
                continue
            else:
                print("Opción inválida. Por favor, elija nuevamente.")

        elif opcion == "2":
            # Lógica para registrar usuario
            nombre = input("Ingrese el nombre del usuario: ")
            apellido = input("Ingrese el apellido del usuario: ")
            telefono = input("Ingrese el número de teléfono del usuario: ")
            correo = input("Ingrese el correo electrónico del usuario: ")
            contrasena = input("Ingrese la contraseña del usuario: ")
            Usuario.registrar_usuario(nombre, apellido, telefono, correo, contrasena)
            # print("Registrando usuario...")
    
        elif opcion == "3":
            # Lógica para ver listado de películas
            print("Mostrando listado de películas...")
    
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, elija nuevamente.")

mostrar_menu()
        

