# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 11:04:35 2023

@author: Erick
"""

import xml.etree.ElementTree as ET

class Cliente:
    pass

    def iniciar_sesion(correo, contrasena):
        # Cargar el archivo XML de usuarios
        tree = ET.parse("usuarios.xml")
        root = tree.getroot()
        
        # Buscar el usuario con el correo y contraseña ingresados
        for usuario in root.findall("usuario"):
            rol = usuario.find("rol").text
            if rol == "cliente":
                correo_actual = usuario.find("correo").text
                contrasena_actual = usuario.find("contrasena").text
                if correo_actual == correo and contrasena_actual == contrasena:
                    # nombre = usuario.find("nombre").text
                    # apellido = usuario.find("apellido").text
                    # telefono = usuario.find("telefono").text
                    print("Inicio de sesión exitoso")
                    print("Rol: Cliente")
                    while True:
                        print("\n--- Cliente ---")
                        print("1. Ver listado de películas")
                        print("2. Listado de películas favoritas")
                        print("3. Comprar boletos")
                        print("4. Historial de boletos comprados")
                        print("5. Cerrar sesión")
                        opcion = input("Ingrese una opción: ")

                        if opcion == "1":
                            # Lógica para ver listado de películas
                            print("Mostrando listado de películas...")
                        elif opcion == "2":
                            # Lógica para ver listado de películas favoritas
                            print("Mostrando listado de películas favoritas...")
                        elif opcion == "3":
                            # Lógica para comprar boletos
                            print("Comprando boletos...")
                        elif opcion == "4":
                            # Lógica para ver historial de boletos comprados
                            print("Mostrando historial de boletos comprados...")
                        elif opcion == "5":
                            break
                        else:
                            print("Opción inválida. Por favor, elija nuevamente.")
                    # print("Nombre:", nombre)
                    # print("Apellido:", apellido)
                    # print("Teléfono:", telefono)
                    return
        
        print("Error: correo o contraseña inválidos")
    
    # Ejemplo de inicio de sesión
    # correo = input("Ingrese su correo electrónico: ")
    # contrasena = input("Ingrese su contraseña: ")
    
    # iniciar_sesion(correo, contrasena)
