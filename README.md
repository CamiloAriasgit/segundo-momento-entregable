# Análisis de Datos de una Tienda de Libros Online

## Descripción del Proyecto

Este proyecto es una aplicación de análisis de datos en Python que procesa información de una tienda de libros en línea. Utiliza la librería **pandas** para limpiar y preparar datos de ventas y libros, y luego realiza operaciones clave para responder a preguntas de negocio. El flujo de trabajo del proyecto sigue la metodología **Git Flow**, garantizando un desarrollo modular y organizado.

---

## Estructura de Archivos

El repositorio está organizado de la siguiente manera:

* `data/`: Contiene los archivos de datos brutos (`libros.csv` y `ventas.csv`).
* `src/`: Contiene el código fuente modularizado, incluyendo el módulo de preprocesamiento de datos (`preprocesamiento.py`).
* `analisis.py`: El script principal que utiliza el módulo de preprocesamiento para realizar el análisis y generar los resultados.

---

## Configuración del Entorno

Sigue estos pasos para configurar tu entorno de desarrollo y ejecutar el proyecto:

1.  **Clona el repositorio:**
    ```bash
    git clone [https://github.com/CamiloAriasgit/segundo-momento-entregable.git](https://github.com/CamiloAriasgit/segundo-momento-entregable.git)
    cd nombre-del-repo
    ```
2.  **Crea y activa un entorno virtual:**
    ```bash
    python -m venv .venv
    .\.venv\Scripts\activate.ps1
    ```
3.  **Instala las dependencias necesarias:**
    ```bash
    pip install pandas
    ```

---

## Ejecución del Script

Para ejecutar el análisis de datos, simplemente corre el script principal en tu terminal:

1.  Asegúrate de tener el entorno virtual activado.
2.  Ejecuta el script de Python:
    ```bash
    python analisis.py
    ```

Los resultados de los análisis, incluyendo las respuestas a las preguntas clave del proyecto, se imprimirán directamente en la consola.

---

## Análisis Realizados

El script `analisis.py` responde a las siguientes preguntas clave:

1.  **Análisis de Frecuencia:** ¿Cuál es el libro con la mayor cantidad de registros o transacciones vendidas?
2.  **Análisis de Agregación:** ¿Cuál es la calificación promedio de los libros por género?
3.  **Análisis con Filtrado y Conteo:** ¿Cuántos libros del autor 'Gabriel García Márquez' se vendieron en total?