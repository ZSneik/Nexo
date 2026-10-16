proyectos = []
siguiente_id = 1

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
        print("Proyecto eliminado correctamente.")
        return True
    else:
        print("Eliminación cancelada.")
        return False

def editar_proyecto(proyecto):
    print("\n========== EDITAR PROYECTO ==========")

    nuevo_nombre = input("Nuevo nombre: ")
    nueva_descripcion = input("Nueva descripcion: ")

    proyecto["nombre"] = nuevo_nombre
    proyecto["descripcion"] = nueva_descripcion

    print("Proyecto actualizado correctamente.")

def menu_proyecto(proyecto):
    while True:
        print(f"\n========== MENU PROYECTO: {proyecto['nombre']} ==========")
        print("1: Ver detalles del proyecto")
        print("2: Editar proyecto")
        print("3: Eliminar proyecto")
        print("4: Volver al menu principal")

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
