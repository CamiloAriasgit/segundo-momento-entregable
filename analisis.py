import pandas as pd
from src.preprocesamiento import cargar_datos, manejar_nulos, estandarizar_texto, limpiar_precios

df_libros = cargar_datos('data/libros.csv')
df_ventas = cargar_datos('data/ventas.csv')

df_libros = manejar_nulos(df_libros, estrategia='media')
df_libros = manejar_nulos(df_libros, estrategia='valor_fijo')
df_libros = estandarizar_texto(df_libros, columnas=['Titulo', 'Autor', 'Genero'])
df_libros = limpiar_precios(df_libros, 'Precio')

df_completo = pd.merge(df_ventas, df_libros, on='ID_Libro', how='inner')

print("--- Respuestas a las preguntas de análisis ---")

print("\nPregunta 1: ¿Cuál es el libro más vendido?")
libro_mas_vendido = df_completo.groupby('Titulo')['Cantidad_Vendida'].sum().idxmax()
print(f"El libro más vendido es: '{libro_mas_vendido}'")

print("\nPregunta 2: ¿Cuál es la calificación promedio de los libros por género?")
calificacion_promedio_por_genero = df_completo.groupby('Genero')['Calificacion'].mean().sort_values(ascending=False)
print("Calificación promedio por género:")
print(calificacion_promedio_por_genero)

print("\nPregunta 3: ¿Cuántos libros del autor 'Gabriel García Márquez' se vendieron?")
ventas_marquez = df_completo[df_completo['Autor'] == 'gabriel garcía márquez']['Cantidad_Vendida'].sum()
print(f"Se vendieron un total de {ventas_marquez} libros de Gabriel García Márquez.")