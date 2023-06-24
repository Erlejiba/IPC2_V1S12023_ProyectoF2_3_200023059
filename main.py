# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 07:17:56 2023

@author: Erick
"""

from peliculas import Pelicula
from administradores import Administrador
from clientes import Cliente


def menu_principal():
    print('\n***************************************************',
          '\n***************************************************',
          '\n             +++++ USAC CINEMA +++++'
          '\n'
          '\n*MENU DE OPCIONES*'
          '\n'
          '\n1. Iniciar sesión',
          '\n2. Registrar usuario',
          '\n3. Ver listado de peliculas',
          '\n4. Salir del programa'
          '\n'
          '\n***************************************************',
          '\n***************************************************')
    
def menu_iniciar_sesion():
    print('\n\n->INICIAR SESION:',
          '\n   1. Administrador',
          '\n   2. Cliente',
          '\n   3. Regresar al menú principal')

def imprimir_menu_principal():
    while True:
        menu_principal()
        opcion_principal = input('\nSeleccione una opción del 1 al 4: ')
        
        if opcion_principal == '1':
            imprimir_iniciar_sesion()
        elif opcion_principal == '2':      
            print("->REGISTRAR USUARIO")
        elif opcion_principal == '3':
            print("\n\n->LISTADO DE PELICULAS")
            pelicula = Pelicula()
            pelicula.lista()
            input()
        elif opcion_principal == '4':
            print('\n\n->SALIENDO DEL PROGRAMA')
            break
        else:
            print("\n\n*Opción inválida*")  
            
def imprimir_iniciar_sesion():
    while True:
        menu_iniciar_sesion()
        opcion_iniciar_sesion = input('\nSeleccione una opción del 1 al 3: ')
        
        if opcion_iniciar_sesion == '1':
            # print('-> Opción 1')         
            usuario_admin = Administrador("admin1@usac.edu.com", "contrasena1")
            usuario_admin.iniciar_sesion_admin()
        elif opcion_iniciar_sesion == '2':
            # print('-> Opción 2')
            usuario_cliente = Cliente("cliente1@usac.edu.com", "contrasena2")
            usuario_cliente.iniciar_sesion_cliente()
        elif opcion_iniciar_sesion == '3':
            break
        else:
            print("\n\n*Opción inválida*")            

imprimir_menu_principal()











    


