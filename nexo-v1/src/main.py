proyectos = []
siguiente_id = 1
estados_tarea=["pendiente", "en_proceso", "completada"]

import json
import os

CARPETA_PROGRAMA = os.path.dirname(os.path.abspath(__file__))
ARCHIVO_DATOS = os.path.join(CARPETA_PROGRAMA, "datos.json")


def guardar_datos():
    datos = {
        "proyectos": proyectos,
        "siguiente_id": siguiente_id
    }

    with open(ARCHIVO_DATOS, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, ensure_ascii=False, indent=4)


def cargar_datos():
    global proyectos, siguiente_id

    if not os.path.exists(ARCHIVO_DATOS):
        return

    try:
        with open(ARCHIVO_DATOS, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        proyectos = datos.get("proyectos", [])
        siguiente_id = datos.get("siguiente_id", 1)

    except json.JSONDecodeError:
        print("Error: el archivo datos.json contiene datos inválidos.")
        print("No se han cargado los datos.")


def crear_proyecto():
    global siguiente_id

    print("\n========== CREAR PROYECTO ==========")

    nombre = input("Ingrese el nombre del proyecto: ")
    descripcion = input("Ingrese la descripcion del proyecto: ")

    proyecto = {
        "id": siguiente_id,
        "nombre": nombre,
        "descripcion": descripcion,
        "tareas": []
    }

    proyectos.append(proyecto)
    siguiente_id += 1
    guardar_datos()

    print("\nProyecto creado correctamente.")
    print("Nombre:", nombre)
    print("Descripcion:", descripcion)
    print("Proyectos en memoria:", proyectos)



def abrir_proyecto():
    print("\n========== ABRIR PROYECTO ==========")

    if not proyectos:
        print("No hay proyectos disponibles.")
        return

    ver_proyectos()

    try:
        input_id = int(input("Ingrese el ID del proyecto que desea abrir: "))
    except ValueError:
        print("El ID debe ser un numero entero.")
        return

    for proyecto in proyectos:
        if proyecto["id"] == input_id:
            menu_proyecto(proyecto)
            return

    print("No se encontro el proyecto con el ID ingresado.")


def eliminar_proyecto(proyecto):
    print("\n========== ELIMINAR PROYECTO ==========")
    confirmacion = input(f"¿Está seguro de que desea eliminar el proyecto '{proyecto['nombre']}'? (s/n): ")

    if confirmacion.lower() == 's':
        proyectos.remove(proyecto)
        guardar_datos()
        print("Proyecto eliminado correctamente.")
        return True
    else:
        print("Eliminación cancelada.")
        return False

def editar_proyecto(proyecto):
    print("\n========== EDITAR PROYECTO ==========")

    nuevo_nombre = input("Nuevo nombre: ").strip()

    if not nuevo_nombre:
        print("El nombre no puede estar vacio.")
        return

    nueva_descripcion = proyecto["descripcion"]

    editar_desc = input("¿Desea editar la descripcion? (s/n): ")

    if editar_desc.lower() == "s":
        nueva_descripcion = input("Nueva descripcion: ").strip()
    else:
        print("Descripcion no editada.")

    print("\nLos nuevos datos del proyecto son:")
    print(f"Nombre: {nuevo_nombre}")
    print(f"Descripcion: {nueva_descripcion}")

    confirmar = input("\n¿Desea guardar los cambios? (s/n): ")

    if confirmar.lower() == "s":
        proyecto["nombre"] = nuevo_nombre
        proyecto["descripcion"] = nueva_descripcion
        guardar_datos()
        print("Proyecto actualizado correctamente.")
    else:
        print("Edicion cancelada. No se realizaron cambios.")

def crear_tarea(proyecto):
    print("\n========== CREAR TAREA ==========")

    nombre = input("Ingrese el nombre de la tarea: ").strip()

    if not nombre:
        print("El nombre no puede estar vacio.")
        return

    descripcion = input("Ingrese la descripcion de la tarea: ").strip()

    tarea = {
        "id": len(proyecto["tareas"]) + 1,
        "nombre": nombre,
        "descripcion": descripcion,
        "estado": "pendiente"
    }

    proyecto["tareas"].append(tarea)
    guardar_datos()

    print("\nTarea creada correctamente.")
    print("ID:", tarea["id"])
    print("Nombre:", tarea["nombre"])
    print("Descripcion:", tarea["descripcion"])
    print("Estado:", tarea["estado"])
    


def editar_tarea(tarea):
    print("\n========== EDITAR TAREA ==========")
    print("Deja el nombre o la descripcion vacios para conservarlos.")

    nuevo_nombre = input("Nuevo nombre: ").strip()
    nueva_descripcion = input("Nueva descripcion: ").strip()

    print("\nEstado actual:", tarea["estado"])
    print("Seleccione el nuevo estado:")
    print("0: Mantener estado actual")
    print("1: Pendiente")
    print("2: En proceso")
    print("3: Completada")

    opcion_estado = input("Ingrese una opcion: ")

    if opcion_estado not in ("0", "1", "2", "3"):
        print("Opcion no valida. No se realizaron cambios.")
        return

    if nuevo_nombre:
        tarea["nombre"] = nuevo_nombre

    if nueva_descripcion:
        tarea["descripcion"] = nueva_descripcion

    if opcion_estado != "0":
        tarea["estado"] = estados_tarea[int(opcion_estado) - 1]
    guardar_datos()

    print("\nTarea actualizada correctamente.")
    print("Nombre:", tarea["nombre"])
    print("Descripcion:", tarea["descripcion"])
    print("Estado:", tarea["estado"])


def menu_tareas(tarea):
    while True:
        print(f"\n========== MENU TAREA: {tarea['nombre']} ==========")
        print("1: Ver detalles de la tarea")
        print("2: Editar tarea")
        print("3: Volver al menu del proyecto")

        opcion = input("Ingrese una opcion: ")

        match opcion:
            case "1":
                print("\n========== DETALLES DE LA TAREA ==========")
                print(f"ID: {tarea['id']}")
                print(f"Nombre: {tarea['nombre']}")
                print(f"Descripcion: {tarea['descripcion']}")
                print(f"Estado: {tarea['estado']}")

            case "2":
                editar_tarea(tarea)

            case "3":
                break

            case _:
                print("Opcion no valida.")

def ver_tareas_completadas(proyecto):
    print("\n========== TAREAS COMPLETADAS ==========")

    tareas_completadas = [
        tarea for tarea in proyecto["tareas"]
        if tarea["estado"] == "completada"
    ]

    if not tareas_completadas:
        print("No hay tareas completadas en este proyecto.")
        return

    # Mostrar un resumen de las tareas completadas
    for tarea in tareas_completadas:
        print(
            f"ID: {tarea['id']} | "
            f"Nombre: {tarea['nombre']} | "
            f"Estado: {tarea['estado']}"
        )

    detalles = input(
        "\n¿Desea consultar una tarea completada? (s/n): "
    )

    if detalles.lower() == "s":
        while True:
            id_tarea = int(input(
                "Ingrese el ID de la tarea que desea abrir (0 para volver): "
            ))

            if id_tarea == 0:
                break

            for tarea in tareas_completadas:
                if tarea["id"] == id_tarea:
                    menu_tareas(tarea)
                    break
            else:
                print("No se encontró esa tarea.")
    

def menu_proyecto(proyecto):
    while True:
        print(f"\n========== MENU PROYECTO: {proyecto['nombre']} ==========")
        print("1: Ver detalles del proyecto")
        print("2: Editar proyecto")
        print("3: Eliminar proyecto")
        print("4: Crear tarea")
        print("5: Ver tareas")
        print("6: Ver historial de tareas")
        print("7: Volver al menu principal")

        opcion = input("Ingrese una opcion: ")

        match opcion:
            case "1":
                print("\n========== DETALLES DEL PROYECTO ==========")
                print(f"ID: {proyecto['id']}")
                print(f"Nombre: {proyecto['nombre']}")
                print(f"Descripcion: {proyecto['descripcion']}")

            case "2":
                editar_proyecto(proyecto)

            case "3":
                if eliminar_proyecto(proyecto):
                    break  
            case "4":
                crear_tarea(proyecto)
            
            case "5":
                if not proyecto["tareas"]:
                    print("No hay tareas disponibles en este proyecto.")
                else:
                    print("\n========== TAREAS DEL PROYECTO ==========")

                    for tarea in proyecto["tareas"]:
                        print(
                            f"ID: {tarea['id']} | "
                            f"Nombre: {tarea['nombre']} | "
                            f"Estado: {tarea['estado']}"
                        )

                    try:
                        id_tarea = int(input("\nIngrese el ID de la tarea que desea abrir (0 para volver): "))
                    except ValueError:
                        print("El ID debe ser un numero entero.")
                        break

                    if id_tarea == 0:
                        break

                    for tarea in proyecto["tareas"]:
                        if tarea["id"] == id_tarea:
                            menu_tareas(tarea)
                            break
                    else:
                        print("No se encontro una tarea con ese ID.")

            case "6":
                ver_tareas_completadas(proyecto)

            case "7":
                break

            case _:
                print("Opcion no valida.")


def ver_proyectos():
    print("\n========== VER PROYECTOS ==========")
    if not proyectos:
        print("No hay proyectos disponibles.")
    else:
        for proyecto in proyectos:
            print(f"ID: {proyecto['id']}, Nombre: {proyecto['nombre']}, Descripcion: {proyecto['descripcion']}")



def menu_principal():
    print("========== NEXO v1 ==========")
    print("Sistema de gestion de proyectos")
    print()
    print("1: Crear proyecto")
    print("2: Abrir proyecto")
    print("3: Ver proyectos")
    print("4: Salir")
    print()
    print("========== version 1.0 ==========")

    opcion = input("Ingrese una opcion: ")
    return opcion

cargar_datos()

iniciar_programa = True

while iniciar_programa:
    opcion = menu_principal()

    match opcion:
        case "1":
            crear_proyecto()
        case "2":
            abrir_proyecto()
        case "3":
            ver_proyectos()
        case "4":
            print("Cerrando Nexo...")
            iniciar_programa = False
        case _:
            print("Opcion no valida")