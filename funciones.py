"""
Actividad DUOC UC - Debugging con Python
Archivo de funciones: funciones.py

Este archivo contiene las funciones del CRUD.
Tiene errores intencionales de sintaxis, lógica y uso de parámetros.
"""

def agregar_estudiante(estudiantes):
    print("\n--- Agregar estudiante ---")
    while True:
        rut = input("Ingrese RUT: ")

        rut_duplicado = False
        for e in estudiantes:
            if e["rut"] == rut:
                rut_duplicado = True
                break
        if rut_duplicado:
            print("Error: este RUT ya se encuentra registrado. Intente con otro. ")
        else:
            break        

    nombre = input("Ingrese nombre: ")
    carrera = input("Ingrese carrera: ")
    while True:
            try:
                edad = int(input("Ingrese edad: "))
                
                if edad > 0:
                    break
                else:
                    print("Error: La edad debe ser mayor a 0.")
                    
            except ValueError:
                print("Error: Por favor, ingrese un valor numérico válido.")

    estudiante = {
        "rut": rut,
        "nombre": nombre,
        "carrera": carrera,
        "edad": edad
    }

    estudiantes.append(estudiante)
    print("Estudiante agregado correctamente")


def listar_estudiantes(estudiantes):
    print("\n--- Lista de estudiantes ---")

    if len(estudiantes) == 0:
        print("No hay estudiantes registrados")
    else:
        for i in range(len(estudiantes)):
            print(f"RUT: {estudiantes[i]['rut']}")
            print(f"Nombre: {estudiantes[i]['nombre']}")
            print(f"Carrera: {estudiantes[i]['carrera']}")
            print(f"Edad: {estudiantes[i]['edad']}")
            print("------------------------")


def buscar_estudiante(estudiantes, rut):
    print("\n--- Buscar estudiante ---")

    encontrado = False

    for estudiante in estudiantes:
        if estudiante["rut"] == rut:
            print("Estudiante encontrado")
            print(f"RUT: {estudiante['rut']}")
            print(f"Nombre: {estudiante['nombre']}")
            print(f"Carrera: {estudiante['carrera']}")
            print(f"Edad: {estudiante['edad']}")
            encontrado = True

    if encontrado == False:
        print("No se encontró el estudiante")


def actualizar_estudiante(estudiantes, rut):
    print("\n--- Actualizar estudiante ---")

    for estudiante in estudiantes:
        if estudiante["rut"] == rut:
            nuevo_nombre = input("Ingrese nuevo nombre: ")
            nueva_carrera = input("Ingrese nueva carrera: ")
            nueva_edad = input("Ingrese nueva edad: ")

            estudiante["nombre"] = nuevo_nombre
            estudiante["carrera"] = nueva_carrera
            estudiante["edad"] == nueva_edad

            print("Estudiante actualizado correctamente")
            return

    print("No se encontró el estudiante")


def eliminar_estudiante(estudiantes, rut):
    print("\n--- Eliminar estudiante ---")

    for estudiante in estudiantes:
        if estudiante["rut"] == rut:
            estudiantes.remove(estudiante)
            print("Estudiante eliminado correctamente")
            return

    print("No se encontró el estudiante")
