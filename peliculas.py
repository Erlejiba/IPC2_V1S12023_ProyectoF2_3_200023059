# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 10:28:41 2023

@author: Erick
"""

import xml.etree.ElementTree as ET

class Pelicula:
    def __init__(self, titulo, director, anio, fecha, hora):
        self.titulo = titulo
        self.director = director
        self.anio = anio
        self.fecha = fecha
        self.hora = hora
        self.siguiente = None
        self.anterior = None

class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre
        self.peliculas = None

class ListaPeliculas:
    def __init__(self):
        self.head = None
        self.tail = None

    def agregar_pelicula(self, titulo, director, anio, fecha, hora):
        nueva_pelicula = Pelicula(titulo, director, anio, fecha, hora)
        if not self.head:
            self.head = nueva_pelicula
            self.tail = nueva_pelicula
        else:
            nueva_pelicula.anterior = self.tail
            self.tail.siguiente = nueva_pelicula
            self.tail = nueva_pelicula

    def mostrar_peliculas(self):
        pelicula_actual = self.head
        while pelicula_actual:
            print("Título:", pelicula_actual.titulo)
            print("Director:", pelicula_actual.director)
            print("Año:", pelicula_actual.anio)
            print("Fecha:", pelicula_actual.fecha)
            print("Hora:", pelicula_actual.hora)
            print("---------------------------")
            pelicula_actual = pelicula_actual.siguiente

def cargar_peliculas_desde_xml():
    lista_peliculas = ListaPeliculas()

    tree = ET.parse("peliculas.xml")
    root = tree.getroot()

    for categoria in root.iter("categoria"):
        nombre_categoria = categoria.find("nombre").text
        nueva_categoria = Categoria(nombre_categoria)
        peliculas = categoria.find("peliculas")
        for pelicula in peliculas.iter("pelicula"):
            titulo = pelicula.find("titulo").text
            director = pelicula.find("director").text
            anio = pelicula.find("anio").text
            fecha = pelicula.find("fecha").text
            hora = pelicula.find("hora").text
            nueva_categoria.peliculas = lista_peliculas
            lista_peliculas.agregar_pelicula(titulo, director, anio, fecha, hora)

    return lista_peliculas

def mostrar_listado_peliculas_por_categoria(lista_peliculas):
    pelicula_actual = lista_peliculas.head
    categoria_actual = None
    while pelicula_actual:
        if pelicula_actual.anterior is None or pelicula_actual.anterior.director != pelicula_actual.director:
            categoria_actual = pelicula_actual.director
            print("\n---", categoria_actual, "---")
            print("Título:", pelicula_actual.titulo)
            print("Director:", pelicula_actual.director)
            print("Año:", pelicula_actual.anio)
            print("Fecha:", pelicula_actual.fecha)
            print("Hora:", pelicula_actual.hora)
        pelicula_actual = pelicula_actual.siguiente

def mostrar_detalle_pelicula_seleccionada(lista_peliculas, titulo_pelicula):
    pelicula_actual = lista_peliculas.head
    while pelicula_actual:
        if pelicula_actual.titulo.lower() == titulo_pelicula.lower():
            print("\n--- Detalle de la película seleccionada ---")
            print("Título:", pelicula_actual.titulo)
            print("Director:", pelicula_actual.director)
            print("Año:", pelicula_actual.anio)
            print("Fecha:", pelicula_actual.fecha)
            print("Hora:", pelicula_actual.hora)
            return
        pelicula_actual = pelicula_actual.siguiente
    print("La película", titulo_pelicula, "no fue encontrada.")

lista_peliculas = cargar_peliculas_desde_xml()
mostrar_listado_peliculas_por_categoria(lista_peliculas)
titulo_seleccionado = input("\nIngrese el título de la película que desea ver en detalle: ")
mostrar_detalle_pelicula_seleccionada(lista_peliculas, titulo_seleccionado)