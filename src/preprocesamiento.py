import pandas as pd
import numpy as np

def cargar_datos(ruta_archivo):
    try:
        if ruta_archivo.endswith('.csv'):
            df = pd.read_csv(ruta_archivo)
        elif ruta_archivo.endswith('.json'):
            df = pd.read_json(ruta_archivo)
        else:
            return None
        return df
    except FileNotFoundError:
        return None
    except Exception as e:
        return None

def manejar_nulos(df, estrategia='media'):
    df_limpio = df.copy()
    if estrategia == 'media':
        for col in df_limpio.columns:
            if df_limpio[col].dtype in ['float64', 'int64']:
                df_limpio[col].fillna(df_limpio[col].mean(), inplace=True)
    elif estrategia == 'moda':
        for col in df_limpio.columns:
            df_limpio[col].fillna(df_limpio[col].mode()[0], inplace=True)
    elif estrategia == 'valor_fijo':
        for col in df_limpio.columns:
            if df_limpio[col].dtype == 'object':
                df_limpio[col].fillna('Desconocido', inplace=True)
    return df_limpio

def estandarizar_texto(df, columnas):
    df_estandarizado = df.copy()
    for col in columnas:
        if col in df_estandarizado.columns and df_estandarizado[col].dtype == 'object':
            df_estandarizado[col] = df_estandarizado[col].str.lower().str.strip()
    return df_estandarizado

def limpiar_precios(df, columna):
    df_limpio = df.copy()
    if columna in df_limpio.columns:
        df_limpio[columna] = df_limpio[columna].str.replace('$', '', regex=False).astype(float)
    return df_limpio