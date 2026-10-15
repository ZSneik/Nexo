
#include <stdio.h>
#include <string.h>
#include "proyectos.h"

void verProyectos(Proyecto proyectos[], int cantidadProyectos)
{
    printf("Proyectos registrados: %d\n", cantidadProyectos);

    if (cantidadProyectos > 0)
    {
        for (int i = 0; i < cantidadProyectos; i++)
        {
            printf("ID: %d\n", proyectos[i].id);
            printf("Nombre: %s\n", proyectos[i].nombre);
            printf("Descripcion: %s\n", proyectos[i].descripcion);
            printf("-------------------------\n");
        }
    }
    else
    {
        printf("No hay proyectos registrados.\n");
    }
}

void crearProyecto(Proyecto proyectos[], int *cantidadProyectos)
{
    printf("Proyectos registrados: %d\n", *cantidadProyectos);

    if (*cantidadProyectos < MAX_PROYECTOS)
    {
        int indice = *cantidadProyectos;

        proyectos[indice].id = indice + 1;

        int caracter;
        while ((caracter = getchar()) != '\n' && caracter != EOF)
        {
        }

        printf("Ingrese el nombre del proyecto: ");
        fgets(proyectos[indice].nombre, TAM_NOMBRE, stdin);
        proyectos[indice].nombre[
            strcspn(proyectos[indice].nombre, "\n")
        ] = '\0';

        printf("Ingrese la descripcion del proyecto: ");
        fgets(proyectos[indice].descripcion, TAM_DESCRIPCION, stdin);
        proyectos[indice].descripcion[
            strcspn(proyectos[indice].descripcion, "\n")
        ] = '\0';

        (*cantidadProyectos)++;
    }
    else
    {
        printf("Se alcanzo el limite de proyectos.\n");
    }
}

void abrirProyecto(Proyecto proyectos[], int cantidadProyectos)
{
    if (cantidadProyectos > 0)
    {
        int idProyecto;
        printf("Ingrese el ID del proyecto a abrir: ");
        scanf("%d", &idProyecto);

        if (idProyecto >= 1 && idProyecto <= cantidadProyectos)
        {
            Proyecto proyectoSeleccionado = proyectos[idProyecto - 1];

            printf("Proyecto seleccionado:\n");
            printf("ID: %d\n", proyectoSeleccionado.id);
            printf("Nombre: %s\n", proyectoSeleccionado.nombre);
            printf("Descripcion: %s\n", proyectoSeleccionado.descripcion);
        }
        else
        {
            printf("ID de proyecto no valido.\n");
        }
    }
    else
    {
        printf("No hay proyectos registrados para abrir.\n");
    }
}

void guardarProyectos(Proyecto proyectos[], int cantidadProyectos)
{
    FILE *archivo = fopen("proyectos.dat", "wb");

    if (archivo == NULL)
    {
        printf("Error al abrir el archivo para guardar los proyectos.\n");
        return;
    }

    size_t escritos = fwrite(
        proyectos,
        sizeof(Proyecto),
        cantidadProyectos,
        archivo
    );

    fclose(archivo);

    if (escritos == (size_t)cantidadProyectos)
    {
        printf("Proyectos guardados correctamente.\n");
    }
    else
    {
        printf("Error al guardar todos los proyectos.\n");
    }
}

int cargarProyectos(Proyecto proyectos[])
{
    FILE *archivo = fopen("proyectos.dat", "rb");

    if (archivo == NULL)
    {
        printf("No se encontraron proyectos guardados.\n");
        return 0;
    }

    size_t cargados = fread(
        proyectos,
        sizeof(Proyecto),
        MAX_PROYECTOS,
        archivo
    );

    fclose(archivo);

    printf(
        "Proyectos cargados correctamente. Total de proyectos: %zu\n",
        cargados
    );

    return (int)cargados;
}
