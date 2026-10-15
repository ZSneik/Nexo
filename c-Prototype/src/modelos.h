
#ifndef MODELOS_H
#define MODELOS_H

#define MAX_PROYECTOS 100
#define MAX_TAREAS 500

#define TAM_NOMBRE 80
#define TAM_DESCRIPCION 200
#define TAM_TITULO_TAREA 100

typedef enum {
    PENDIENTE,
    EN_CURSO,
    COMPLETADA
} EstadoTarea;

typedef struct {
    int id;
    char nombre[TAM_NOMBRE];
    char descripcion[TAM_DESCRIPCION];
} Proyecto;

typedef struct {
    int id;
    int proyecto_id;
    char titulo[TAM_TITULO_TAREA];
    EstadoTarea estado;
} Tarea;

#endif
