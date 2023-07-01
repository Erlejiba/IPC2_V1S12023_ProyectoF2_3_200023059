# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 17:11:13 2023

@author: Erick
"""

import xml.etree.ElementTree as ET

class Usuario:
    def __init__(self, rol, nombre, apellido, telefono, correo, contrasena):
        self.rol = rol
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.correo = correo
        self.contrasena = contrasena
        self.siguiente = None
        self.anterior = None
        
    def registrar_usuario(nombre, apellido, telefono, correo, contrasena):
        # Crear el elemento de usuario
        usuario = ET.Element("usuario")
        
        # Crear los elementos internos
        rol = ET.SubElement(usuario, "rol")
        rol.text = "cliente"
        
        nombre_element = ET.SubElement(usuario, "nombre")
        nombre_element.text = nombre
        
        apellido_element = ET.SubElement(usuario, "apellido")
        apellido_element.text = apellido
        
        telefono_element = ET.SubElement(usuario, "telefono")
        telefono_element.text = telefono
        
        correo_element = ET.SubElement(usuario, "correo")
        correo_element.text = correo
        
        contrasena_element = ET.SubElement(usuario, "contrasena")
        contrasena_element.text = contrasena
        
        # Cargar el archivo XML existente
        tree = ET.parse("usuarios.xml")
        root = tree.getroot()
        
        # Agregar el nuevo usuario al XML
        root.append(usuario)
        
        # Guardar los cambios en el archivo XML
        tree.write("usuarios.xml")

class ListaUsuarios:
    def __init__(self):
        self.cabeza = None

    def agregar_usuario(self, usuario):
        if self.cabeza is None:
            self.cabeza = usuario
            usuario.siguiente = usuario
            usuario.anterior = usuario
        else:
            ultimo = self.cabeza.anterior
            ultimo.siguiente = usuario
            usuario.anterior = ultimo
            usuario.siguiente = self.cabeza
            self.cabeza.anterior = usuario

    def buscar_usuario(self, correo):
        if self.cabeza is None:
            return None

        actual = self.cabeza
        while True:
            if actual.correo == correo:
                return actual

            actual = actual.siguiente
            if actual == self.cabeza:
                break

        return None

    def modificar_usuario(self, correo, nuevo_nombre, nuevo_apellido, nuevo_telefono, nueva_contrasena):
        usuario = self.buscar_usuario(correo)
        if usuario is not None:
            usuario.nombre = nuevo_nombre
            usuario.apellido = nuevo_apellido
            usuario.telefono = nuevo_telefono
            usuario.contrasena = nueva_contrasena
            return True

        return False

    def eliminar_usuario(self, correo):
        usuario = self.buscar_usuario(correo)
        if usuario is not None:
            if usuario == self.cabeza:
                if self.cabeza.siguiente == self.cabeza:
                    self.cabeza = None
                else:
                    ultimo = self.cabeza.anterior
                    self.cabeza = self.cabeza.siguiente
                    ultimo.siguiente = self.cabeza
                    self.cabeza.anterior = ultimo
            else:
                anterior = usuario.anterior
                siguiente = usuario.siguiente
                anterior.siguiente = siguiente
                siguiente.anterior = anterior

            return True

        return False

    def mostrar_usuarios(self):
        if self.cabeza is None:
            print("No hay usuarios registrados.")
            return

        actual = self.cabeza
        while True:
            print("Rol:", actual.rol)
            print("Nombre:", actual.nombre)
            print("Apellido:", actual.apellido)
            print("Teléfono:", actual.telefono)
            print("Correo:", actual.correo)
            print("Contraseña:", actual.contrasena)
            print()

            actual = actual.siguiente
            if actual == self.cabeza:
                break

    def guardar_en_xml(self, archivo):
        root = ET.Element("usuarios")

        if self.cabeza is not None:
            actual = self.cabeza
            while True:
                usuario = ET.SubElement(root, "usuario")

                rol = ET.SubElement(usuario, "rol")
                rol.text = actual.rol

                nombre = ET.SubElement(usuario, "nombre")
                nombre.text = actual.nombre

                apellido = ET.SubElement(usuario, "apellido")
                apellido.text = actual.apellido

                telefono = ET.SubElement(usuario, "telefono")
                telefono.text = actual.telefono

                correo = ET.SubElement(usuario, "correo")
                correo.text = actual.correo

                contrasena = ET.SubElement(usuario, "contrasena")
                contrasena.text = actual.contrasena

                actual = actual.siguiente
                if actual == self.cabeza:
                    break

        tree = ET.ElementTree(root)
        tree.write(archivo)

    def cargar_desde_xml(self, archivo):
        tree = ET.parse(archivo)
        root = tree.getroot()

        for usuario_xml in root.findall("usuario"):
            rol = usuario_xml.find("rol").text
            nombre = usuario_xml.find("nombre").text
            apellido = usuario_xml.find("apellido").text
            telefono = usuario_xml.find("telefono").text
            correo = usuario_xml.find("correo").text
            contrasena = usuario_xml.find("contrasena").text

            usuario = Usuario(rol, nombre, apellido, telefono, correo, contrasena)
            self.agregar_usuario(usuario)

# # Ejemplo de uso
# lista_usuarios = ListaUsuarios()

# # Cargar desde el archivo XML
# lista_usuarios.cargar_desde_xml("usuarios.xml")

# # Agregar usuarios
# usuario1 = Usuario("cliente", "John", "Doe", "123456789", "john.doe@example.com", "mipassword123")
# usuario2 = Usuario("administrador", "Jane", "Smith", "987654321", "jane.smith@example.com", "password456")
# lista_usuarios.agregar_usuario(usuario1)
# lista_usuarios.agregar_usuario(usuario2)

# # Modificar un usuario
# lista_usuarios.modificar_usuario("john.doe@example.com", "John", "Smith", "987654321", "newpassword")

# # Eliminar un usuario
# lista_usuarios.eliminar_usuario("jane.smith@example.com")

# # Mostrar la lista de usuarios
# lista_usuarios.mostrar_usuarios()

# # Guardar en el archivo XML
# lista_usuarios.guardar_en_xml("usuarios.xml")