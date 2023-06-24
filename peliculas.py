# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 23:24:22 2023

@author: Erick
"""

class Pelicula:
    def __init__(self):
        pass
    
    def lista(self):
        import xml.etree.ElementTree as ET
        
        tree = ET.parse('peliculas.xml')
        root = tree.getroot()
        
        for categoria in root.findall("categoria"):
            nombre = categoria.find('nombre').text
            print(f"\nNombre: {nombre.strip()}")
            pelicula = categoria.find('peliculas')
            
            for peli in pelicula.findall('pelicula'):
                titulo = peli.find('titulo').text
                print(titulo)
                