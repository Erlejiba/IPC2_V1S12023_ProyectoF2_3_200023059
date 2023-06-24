# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 00:57:06 2023

@author: Erick
"""

from nodoLES import Nodo
from registro import Cine
import xml.etree.ElementTree as ET

class Sala:
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

    def Imprimir1(self):
        actual = self.cabeza
        actual.dato.imprimir()
        while actual.siguiente is not None:
            actual = actual.siguiente
            actual.dato.imprimir()

    def CargarXML1(self, operacion):
        
        tree = ET.parse('salas.xml')
        root = tree.getroot()

        for indice, personas in enumerate(root.findall('cine')):
            nombre = personas.find('nombre').text
            sala = personas.find('salas')                 
            
            for cin in sala.findall('sala'): 
                numero = cin.find('numero').text
                
                numero = personas.find('salas').text
                asientos = cin.find('asientos').text
                       
            objeto = Cine(nombre, numero, asientos)
            
            if operacion == 1: # agregar datos a la lista
                self.add(objeto)
            elif operacion == 2:            
                self.modify(objeto, indice)
            
    def editarXML(self):
        tree = ET.parse('salas.xml')
        root = tree.getroot()

        nombre1 = root.find("usuario[cliente]/nombre")
        nombre1.text = "Johnas"

        tree.write("salas.xml")

        self.CargarXML(2)