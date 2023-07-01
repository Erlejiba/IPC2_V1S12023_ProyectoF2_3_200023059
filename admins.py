# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 11:07:58 2023

@author: Erick
"""

from usuarios import Usuario
from usuarios import ListaUsuarios
import xml.etree.ElementTree as ET


class Admin:
    
    def iniciar_sesion_admin(correo, contrasena):
        # Cargar el archivo XML de usuarios
        tree = ET.parse("usuarios.xml")
        root = tree.getroot()
    
        # Buscar el usuario con el correo y contraseña ingresados
        for usuario in root.findall("usuario"):
            rol = usuario.find("rol").text
            if rol == "administrador":
                correo_actual = usuario.find("correo").text
                contrasena_actual = usuario.find("contrasena").text
                if correo_actual == correo and contrasena_actual == contrasena:
                    # nombre = usuario.find("nombre").text
                    # apellido = usuario.find("apellido").text
                    # telefono = usuario.find("telefono").text
                    print("Inicio de sesión exitoso")
                    print("Rol: Administrador")
                    while True:
                        print("\n--- Administrador ---")
                        print("1. Gestionar usuarios")
                        print("2. Gestionar categorías y películas")
                        print("3. Gestionar salas")
                        print("4. Cerrar sesión")
                        opcion = input("Ingrese una opción: ")
            
                        if opcion == "1":
                            Admin.gestionar_usuarios()
                        elif opcion == "2":
                            pass
                            Admin.gestionar_categorias_peliculas()
                        elif opcion == "3":
                            pass
                            Admin.gestionar_salas()
                        elif opcion == "4":
                            break
                        else:
                            print("Opción inválida. Por favor, elija nuevamente.")
                    return
        # print("Nombre:", nombre)
        # print("Apellido:", apellido)
        # print("Teléfono:", telefono)
                    # return
        print("Error: correo o contraseña inválidos")
        
    
    # Ejemplo de inicio de sesión como administrador
    # correo = input("Ingrese su correo electrónico: ")
    # contrasena = input("Ingrese su contraseña: ")

    # iniciar_sesion_admin(correo, contrasena)
    
    def gestionar_usuarios():
        while True:
            print("\n--- Gestionar usuarios ---")
            print("1. Cargar XML de usuarios")
            print("2. Agregar usuarios")
            print("3. Modificar usuarios")
            print("4. Eliminar usuarios")
            print("5. Regresar al menú anterior")
            opcion = input("Ingrese una opción: ")
            lista_usuarios = ListaUsuarios()
            # usuario = Usuario()
            
            if opcion == "1":
                # Lógica para cargar XML de usuarios
                print("Cargando XML de usuarios...")         
                lista_usuarios.cargar_desde_xml("usuarios.xml")
                lista_usuarios.mostrar_usuarios()       
                
            elif opcion == "2":
                # Lógica para agregar usuarios
                lista_usuarios.cargar_desde_xml("usuarios.xml")
                rol = input("Ingrese el rol del usuario: ")
                nombre = input("Ingrese el nombre del usuario: ")
                apellido = input("Ingrese el apellido del usuario: ")
                telefono = input("Ingrese el teléfono del usuario: ")
                correo = input("Ingrese el correo del usuario: ")
                contrasena = input("Ingrese la contraseña del usuario: ")
                print()
                usuario1 = Usuario(rol, nombre, apellido, telefono, correo, contrasena)
                lista_usuarios.agregar_usuario(usuario1)
                lista_usuarios.mostrar_usuarios()
                lista_usuarios.guardar_en_xml("usuarios.xml")
                        
            elif opcion == "3":
                # Lógica para modificar usuarios
                print("Modificando usuarios...")
            elif opcion == "4":
                # Lógica para eliminar usuarios
                print("Eliminando usuarios...")
            elif opcion == "5":
                break
            else:
                print("Opción inválida. Por favor, elija nuevamente.")


    def gestionar_categorias_peliculas():
        while True:
            print("\n--- Gestionar categorías y películas ---")
            print("1. Cargar XML de categorías y películas")
            print("2. Crear categorías y películas")
            print("3. Modificar categorías y películas")
            print("4. Eliminar categoría y películas")
            print("5. Regresar al menú anterior")
            opcion = input("Ingrese una opción: ")

            if opcion == "1":
                # Lógica para cargar XML de categorías y películas
                print("Cargando XML de categorías y películas...")
            elif opcion == "2":
                # Lógica para crear categorías y películas
                print("Creando categorías y películas...")
            elif opcion == "3":
                # Lógica para modificar categorías y películas
                print("Modificando categorías y películas...")
            elif opcion == "4":
                # Lógica para eliminar categoría y películas
                print("Eliminando categoría y películas...")
            elif opcion == "5":
                break
            else:
                print("Opción inválida. Por favor, elija nuevamente.")


    def gestionar_salas():
        while True:
            print("\n--- Gestionar salas ---")
            print("1. Cargar XML de salas")
            print("2. Crear salas")
            print("3. Modificar salas")
            print("4. Eliminar salas")
            print("5. Regresar al menú anterior")
            opcion = input("Ingrese una opción: ")

            if opcion == "1":
                # Lógica para cargar XML de salas
                print("Cargando XML de salas...")
            elif opcion == "2":
                # Lógica para crear salas
                print("Creando salas...")
            elif opcion == "3":
                # Lógica para modificar salas
                print("Modificando salas...")
            elif opcion == "4":
                # Lógica para eliminar salas
                print("Eliminando salas...")
            elif opcion == "5":
                break
            else:
                print("Opción inválida. Por favor, elija nuevamente.")
    


