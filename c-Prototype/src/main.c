#include <stdio.h>
#include "modelos.h"
#include "proyectos.h"

int main(void)
{
    int cantidadProyectos = 0;
    char opcionMenu = 0;
    char iniciarPrograma = 1;
    Proyecto proyectos[MAX_PROYECTOS];

    cantidadProyectos = cargarProyectos(proyectos);

while (iniciarPrograma)
{
    printf("\n========== NEXO v0.1 ==========\n");
    printf("1: Ver proyectos\n");
    printf("2: Crear proyecto\n");
    printf("3: Abrir proyecto\n");
    printf("0: Salir\n");
    printf("Seleccione una opcion: ");

    if (scanf("%hhd", &opcionMenu) != 1)
    {
        printf("Entrada no valida. Introduzca un numero.\n");

        int caracter;
        while ((caracter = getchar()) != '\n' && caracter != EOF)
        {

        }

        continue;
    }

    switch (opcionMenu)
    {
        case 1:
            printf("Ver proyectos\n");
            verProyectos(proyectos, cantidadProyectos);
            break;

        case 2:
            printf("Crear proyecto\n");
            crearProyecto(proyectos, &cantidadProyectos);
            guardarProyectos(proyectos, cantidadProyectos);
            break;

        case 3:
            printf("Abrir proyecto\n");
            abrirProyecto(proyectos, cantidadProyectos);
            break;

        case 0:
            iniciarPrograma = 0;
            printf("Cerrando Nexo...\n");
            break;

        default:
            printf("Opcion no valida.\n");
            break;
    }
}

return 0;

}