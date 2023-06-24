# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 07:58:01 2023

@author: Erick
"""

from usuarioLES import Usuario
from salaLES import Sala

def imprimir_crud():
    print('\n           1. Crear',
          '\n           2. Leer',
          '\n           3. Modificar',
          '\n           4. Eliminar'
          '\n           5. Salir')

class Administrador:
    def __init__(self, correo_admin, contrasena_admin):
        self.correo_admin = correo_admin
        self.contrasena_admin = contrasena_admin
            
    def iniciar_sesion_admin(self):
        correo = input("\n\nIngrese su correo electrónico: ")
        contrasena = input("Ingrese su contraseña: ")
    
        
        if correo == self.correo_admin and contrasena == self.contrasena_admin:
            print('\n¡BIENVENIDO! \|/ INICIO DE SESION EXITOSO \|/')
            while True:
                print('\n       1. Gestionar usuarios',
                      '\n       2. Gestionar categoraias y peliculas',
                      '\n       3. Gestionar salas'
                      '\n       4. Cerrar sesión')
            
                opcion_admin = input('\nSeleccione una opción del 1 al 4: ')
                
                if opcion_admin == '1':
                    while True:
                        print('\n->GESTIONAR USUARIOS')
                        imprimir_crud()
                        opcion_crud = input('\nSeleccione una opción del 1 al 5: ')
                        if opcion_crud == '1':
                            print('\n\n->CREAR')
                            input()
                        elif opcion_crud == '2':      
                            print('\n\n->LEER')
                            lista_usuarios = Usuario()
                            lista_usuarios.CargarXML(1)
                            lista_usuarios.Imprimir()
                            input()
                        elif opcion_crud == '3':
                            print('\n\n->MODIFICAR')
                            input()
                        elif opcion_crud == '4':
                            print('\n\n->ELIMINAR')
                            input()
                        elif opcion_crud == '5':
                            print('\n\n->SALIENDO')
                            break
                        else:
                            print('\n\n*Opción inválida*')

                elif opcion_admin == '2':     
                    while True:
                        print('-\n\n>GESTIONAR CATEGORIAS Y PELICULAS')
                        imprimir_crud()
                        opcion_crud = input('\nSeleccione una opción del 1 al 5: ')
                        if opcion_crud == '1':
                            print('\n\n->CREAR')
                            input()
                        elif opcion_crud == '2':      
                            print('\n\n->LEER')
                            # lista_salas = Sala()
                            # lista_salas.CargarXML(1)
                            # lista_salas.Imprimir()
                            input()
                        elif opcion_crud == '3':
                            print('\n\n->MODIFICAR')
                            input()
                        elif opcion_crud == '4':
                            print('\n\n->ELIMINAR')
                            input()
                        elif opcion_crud == '5':
                            print('\n\n->SALIENDO')
                            break
                        else:
                            print('\n\n*Opción inválida*')

                        
                elif opcion_admin == '3':
                    while True:
                        print('\n\n->GESTIONAR SALAS')
                        imprimir_crud()
                        opcion_crud = input('\nSeleccione una opción del 1 al 5: ')
                        if opcion_crud == '1':
                            print('\n\n->CREAR')
                            input()
                        elif opcion_crud == '2':      
                            print('\n\n->LEER')
                            lista_salas = Sala()
                            lista_salas.CargarXML1(1)
                            lista_salas.Imprimir1()
                            input()
                        elif opcion_crud == '3':
                            print('\n\n->MODIFICAR')
                            input()
                        elif opcion_crud == '4':
                            print('\n\n->ELIMINAR')
                            input()
                        elif opcion_crud == '5':
                            print('\n\n->SALIENDO')
                            break
                        else:
                            print('\n\n*Opción inválida*')
                    
                elif opcion_admin == '4':
                    print('\n\n->SESION CERRADA')
                    
                    break
                else:
                    print('\n\n*Opción inválida*')
        else:
            print("\n-----Correo o contraseña incorrectos-----")
