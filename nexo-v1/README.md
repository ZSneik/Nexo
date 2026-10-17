# Nexo

**Un gestor de proyectos en desarrollo, construido como parte de mi formación en programación.**

Nexo es un proyecto personal orientado a la gestión de proyectos desde una interfaz de línea de comandos. Su objetivo es evolucionar progresivamente hacia una herramienta que permita organizar proyectos, administrar tareas y conservar información de manera persistente.

El proyecto comenzó con un prototipo desarrollado en C y continuó con una nueva versión en Python. Esta transición forma parte de mi proceso de aprendizaje: comprender cómo se construye un programa, cómo se organiza su lógica y cómo transformar una idea inicial en una aplicación funcional y ampliable.

Actualmente, Nexo se encuentra en una etapa inicial de desarrollo. La versión Python implementa las operaciones básicas de gestión de proyectos y sirve como base para incorporar nuevas funcionalidades.

## Objetivos del proyecto

- Construir una aplicación funcional a partir de una idea propia.
- Desarrollar habilidades de programación mediante la implementación de funcionalidades concretas.
- Practicar la organización del código, la validación de entradas y el control del flujo de ejecución.
- Aprender a representar y administrar información mediante estructuras de datos.
- Evolucionar desde una aplicación sencilla en consola hacia un sistema más completo y mantenible.
- Documentar el proceso de desarrollo y utilizar Git y GitHub para gestionar el código fuente.

## Funcionalidades actuales

La versión Python permite:

- **Crear proyectos:** registrar un nombre, una descripción y un identificador.
- **Listar proyectos:** consultar los proyectos registrados durante la ejecución.
- **Abrir proyectos:** acceder a un menú individual para cada proyecto.
- **Consultar detalles:** visualizar el identificador, el nombre y la descripción.
- **Editar proyectos:** modificar el nombre y, opcionalmente, la descripción, con confirmación antes de guardar los cambios.
- **Eliminar proyectos:** solicitar confirmación antes de eliminarlos.
- **Navegar por menús interactivos:** utilizar opciones para acceder a las distintas operaciones y regresar al menú principal.

Los proyectos se administran actualmente en memoria. Por lo tanto, la información se pierde al cerrar el programa.

## Tecnologías y conceptos

- **Python 3:** lenguaje utilizado para la versión actual.
- **VS Code:** entorno de desarrollo.
- **Code Runner:** ejecución del programa desde el editor.
- **Git y GitHub:** control de versiones y publicación del código.

Durante el desarrollo estoy trabajando con:

- Funciones y variables.
- Listas y diccionarios.
- Condicionales y bucles.
- Estructuras `match-case`.
- Entrada y salida por consola.
- Manejo de errores mediante `try-except`.
- Validación de datos introducidos por el usuario.
- Manipulación de estructuras de datos y actualización controlada de su contenido.
- Organización de la lógica mediante funciones y separación de responsabilidades.

## Mi experiencia y motivación

Soy estudiante de Ingeniería Civil Física y estoy desarrollando mis habilidades de programación como parte de una formación orientada a comprender sistemas, resolver problemas y construir herramientas propias.

Mi interés no se limita a aprender la sintaxis de un lenguaje. Quiero entender cómo funciona un programa desde sus fundamentos: cómo se representa la información, cómo se toman decisiones, cómo se controla la ejecución y cómo se relacionan las distintas partes de un sistema.

Nexo me permite trabajar sobre estos conceptos en un contexto práctico. En lugar de limitarme a ejercicios aislados, estoy desarrollando una aplicación que necesita mantener una estructura coherente, responder a las decisiones del usuario y evolucionar sin perder su funcionalidad anterior.

El proyecto también representa una oportunidad para trasladar conocimientos entre lenguajes. La primera aproximación se realizó en C, un lenguaje que me interesa por su relación con la programación de bajo nivel, los microcontroladores y los sistemas embebidos. La versión actual utiliza Python, que me permite avanzar en la construcción de aplicaciones y explorar otras formas de organizar y manipular información.

Esta transición no busca descartar el trabajo anterior, sino continuar el desarrollo desde otra perspectiva. Cada versión constituye una etapa de aprendizaje y una oportunidad para comparar soluciones, comprender sus diferencias y tomar decisiones técnicas más fundamentadas.

Mi enfoque es progresivo: implementar una funcionalidad, comprobar su comportamiento, identificar sus limitaciones y mejorarla antes de ampliar el alcance del programa. De esta manera, busco fortalecer tanto mi capacidad para escribir código como mi criterio para diseñar y mantener software.

## Hoja de ruta

Las siguientes etapas previstas para el proyecto son:

- [x] Crear proyectos con identificador, nombre y descripción.
- [x] Listar los proyectos registrados.
- [x] Abrir un proyecto y consultar sus detalles.
- [x] Editar la información de un proyecto.
- [x] Eliminar proyectos con confirmación.
- [ ] Crear, listar y eliminar tareas dentro de cada proyecto.
- [ ] Permitir cambiar el estado de las tareas.
- [ ] Guardar y recuperar información mediante archivos JSON.
- [ ] Separar el código en módulos a medida que aumente su complejidad.
- [ ] Incorporar pruebas y mejorar el manejo de errores.
- [ ] Ampliar la documentación y evaluar nuevas formas de interacción.

Esta hoja de ruta es orientativa. Las funcionalidades pendientes se incorporarán gradualmente y se actualizarán a medida que estén implementadas.

## Ejecución

### Requisitos

- Python 3.10 o posterior, debido al uso de `match-case`.
- Una terminal o un editor compatible, como Visual Studio Code.

### Ejecutar el programa

Desde la carpeta que contiene `main.py`, ejecuta:

```bash
python3 main.py
```

En Windows también puedes utilizar:

```powershell
py main.py
```

El programa mostrará el menú principal de Nexo y permitirá interactuar con las opciones disponibles.

## Estado del proyecto

Nexo se encuentra en desarrollo activo como proyecto personal de aprendizaje y experimentación.

La versión actual es un prototipo funcional de gestión de proyectos en consola, todavía limitado por la ausencia de persistencia de datos y de un sistema de tareas implementado.

El objetivo a largo plazo es convertirlo en una aplicación más completa, modular y robusta, utilizando cada etapa como