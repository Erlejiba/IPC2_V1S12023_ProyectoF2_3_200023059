# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 16:48:51 2023

@author: Erick
"""

class Cine:
    def __init__(self, nombre, numero, asientos):
        self.nombre = nombre
        self.numero = numero
        self.asientos = asientos
    
    def imprimir(self):
        print(f"Nombre: {self.nombre} Número: {self.numero} Asientos: {self.asientos}")

class Registro:
    def __init__(self, rol, nombre, apellido, telefono, correo, contrasena):
        self.rol = rol
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.correo = correo
        self.contrasena = contrasena
    
    def imprimir(self):
        print(f"Rol: {self.rol} Nombre: {self.nombre} Apellido: {self.apellido} Telefono: {self.telefono} Correo: {self.correo} Contraseña: {self.contrasena}")
        