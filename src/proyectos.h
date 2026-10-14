#ifndef CREARPROYECTOS_H
#define CREARPROYECTOS_H
#include "modelos.h"

void verProyectos(Proyecto proyectos[], int cantidadProyectos);
void crearProyecto(Proyecto proyectos[], int *cantidadProyectos);
void abrirProyecto(Proyecto proyectos[], int cantidadProyectos);
void guardarProyectos(Proyecto proyectos[], int cantidadProyectos);
int cargarProyectos(Proyecto proyectos[]);
#endif 