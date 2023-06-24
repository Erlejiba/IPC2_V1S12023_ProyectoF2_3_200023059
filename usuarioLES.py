from nodoLES import Nodo
from registro import Registro
import xml.etree.ElementTree as ET

class Usuario:
    def __init__(self):
        self.cabeza = None

    def add(self, dato):
        
        nuevo = Nodo(dato)

        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def modify(self, dato_nuevo, index):
        actual = self.cabeza
        indice = 0

        while actual is not None:
            if indice == index:
                actual.dato = dato_nuevo
                return
            indice += 1
            actual = actual.siguiente

    def Imprimir(self):
        actual = self.cabeza
        actual.dato.imprimir()
        while actual.siguiente is not None:
            actual = actual.siguiente
            actual.dato.imprimir()

    def CargarXML(self, operacion):
        
        tree = ET.parse('usuarios.xml')
        root = tree.getroot()

        for indice, personas in enumerate(root.findall('usuario')):
            rol = personas.find('rol').text
            nombre = personas.find('nombre').text
            apellido = personas.find('apellido').text
            telefono = personas.find('telefono').text
            correo = personas.find('correo').text
            contrasena = personas.find('contrasena').text
            
            objeto = Registro(rol, nombre, apellido, telefono, correo, contrasena)
            
            if operacion == 1: # agregar datos a la lista
                self.add(objeto)
            elif operacion == 2:            
                self.modify(objeto, indice)
            
    def editarXML(self):
        tree = ET.parse('usuarios.xml')
        root = tree.getroot()

        nombre1 = root.find("usuario[cliente]/nombre")
        nombre1.text = "Johnas"

        tree.write("usuarios.xml")

        self.CargarXML(2)


