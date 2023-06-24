# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 15:26:13 2023

@author: Erick
"""
from peliculas import Pelicula

class Cliente:
    def __init__(self, correo_cliente, contrasena_cliente):
        self.correo_cliente = correo_cliente
        self.contrasena_cliente = contrasena_cliente
        
        
    def iniciar_sesion_cliente(self):
        correo = input("\n\nIngrese su correo electrónico: ")
        contrasena = input("Ingrese su contraseña: ")

        if correo == self.correo_cliente and contrasena == self.contrasena_cliente:
            print('\n¡BIENVENIDO! \|/ INICIO DE SESION EXITOSO \|/')
            while True:
                print('\n       1. Ver listado de peliculas',
                      '\n       2. Listado de peliculas favoritas',
                      '\n       3. Comprar boletos'
                      '\n       4. Historial de boletos comprados'
                      '\n       5. Cerrar sesión')
            
                opcion_admin = input('\nSeleccione una opción del 1 al 4: ')
                if opcion_admin == '1':
                    print("\n\n->LISTADO DE PELICULAS")
                    pelicula = Pelicula()
                    pelicula.lista()
                    input()
                elif opcion_admin == '2':      
                    print('\n\n->LISTADO DE PELICULAS FAVORITAS')
                    
                elif opcion_admin == '3':
                    print('\n\n->COMPRAR BOLETOS')
                    
                elif opcion_admin == '4':
                    print('\n\n->HISTORIAL DE BOLETOS COMPRADOS')
                    
                elif opcion_admin == '5':
                    print('\n\n->SESION CERRADA')
                    break
                else:
                    print('\n\n*Opción inválida*')
        else:
            print("\n-----Correo o contraseña incorrectos-----")

