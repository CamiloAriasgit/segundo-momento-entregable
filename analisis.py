import pandas as pd
from src.preprocesamiento import cargar_datos, manejar_nulos, estandarizar_texto, limpiar_precios

df_libros = cargar_datos('data/libros.csv')
df_ventas = cargar_datos('data/ventas.csv')

print("--- Diagnóstico inicial de df_libros ---")
df_libros.info()

print("--- Diagnóstico inicial de df_ventas ---")
df_ventas.info()

print("\n--- Limpiando datos de libros ---")
df_libros = manejar_nulos(df_libros, estrategia='media')
df_libros = manejar_nulos(df_libros, estrategia='valor_fijo')
df_libros = estandarizar_texto(df_libros, columnas=['Titulo', 'Autor', 'Genero'])
df_libros = limpiar_precios(df_libros, 'Precio')

print("\n--- Diagnóstico final de df_libros ---")
df_libros.info()

print("\n--- Combinando datos ---")
df_completo = pd.merge(df_ventas, df_libros, on='ID_Libro', how='inner')
df_completo.info()

print("\n--- Realizando análisis ---")
ventas_por_genero = df_completo.groupby('Genero')['Cantidad_Vendida'].sum().sort_values(ascending=False)
print("\n--- Ventas totales por género ---")
print(ventas_por_genero)