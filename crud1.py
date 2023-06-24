# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 23:59:07 2023

@author: Erick
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 23:57:29 2023

@author: Erick
"""

class Tarea:
    def __init__(self, id, titulo, descripcion):
        self.id = id
        self.titulo = titulo
        self.descripcion = descripcion

class ListaTareas:
    def __init__(self):
        self.tareas = []
        self.contador_id = 1

    def agregar_usuario(self, titulo, descripcion):
        tarea = Tarea(self.contador_id, titulo, descripcion)
        self.tareas.append(tarea)
        self.contador_id += 1
        print("Tarea agregada correctamente.")

    def listar_usuario(self):
        if self.Usuarios:
            lista_usuarios = Usuario()
            lista_usuarios.CargarXML(1)
            lista_usuarios.Imprimir()
        # if not self.tareas:
        #     print("No hay tareas en la lista.")
        # else:
        #     print("Lista de tareas:")
        #     for tarea in self.tareas:
        #         print("ID:", tarea.id)
        #         print("Título:", tarea.titulo)
        #         print("Descripción:", tarea.descripcion)
        #         print()

    def editar_tarea(self, id, nuevo_titulo, nueva_descripcion):
        tarea_encontrada = None
        for tarea in self.tareas:
            if tarea.id == id:
                tarea_encontrada = tarea
                break

        if tarea_encontrada:
            tarea_encontrada.titulo = nuevo_titulo
            tarea_encontrada.descripcion = nueva_descripcion
            print("Tarea editada correctamente.")
        else:
            print("No se encontró la tarea con el ID especificado.")

    def eliminar_tarea(self, id):
        tarea_encontrada = None
        for tarea in self.tareas:
            if tarea.id == id:
                tarea_encontrada = tarea
                break

        if tarea_encontrada:
            self.tareas.remove(tarea_encontrada)
            print("Tarea eliminada correctamente.")
        else:
            print("No se encontró la tarea con el ID especificado.")

def mostrar_menu():
    menu = """
    === Menú ===
    1. Agregar tarea
    2. Listar tareas
    3. Editar tarea
    4. Eliminar tarea
    0. Salir
    """

    lista_tareas = ListaTareas()

    while True:
        print(menu)
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo = input("Ingrese el título de la tarea: ")
            descripcion = input("Ingrese la descripción de la tarea: ")
            lista_tareas.agregar_tarea(titulo, descripcion)
        elif opcion == "2":
            lista_tareas.listar_tareas()
        elif opcion == "3":
            id = int(input("Ingrese el ID de la tarea a editar: "))
            nuevo_titulo = input("Ingrese el nuevo título de la tarea: ")
            nueva_descripcion = input("Ingrese la nueva descripción de la tarea: ")
            lista_tareas.editar_tarea(id, nuevo_titulo, nueva_descripcion)
        elif opcion == "4":
            id = int(input("Ingrese el ID de la tarea a eliminar: "))
            lista_tareas.eliminar_tarea(id)
        elif opcion == "0":
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

# Iniciar la aplicación
mostrar_menu()