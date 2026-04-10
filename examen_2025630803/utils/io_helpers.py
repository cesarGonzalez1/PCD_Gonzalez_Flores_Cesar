import os

def leer_csv(ruta):
    filas = []
    try:
        with open(ruta, 'r', encoding='utf-8') as f:
            for linea in f:
                linea_limp = linea.strip()
                
                if not linea_limp:
                    continue
                columnas = linea_limp.split(',')
                filas.append(columnas)
    except FileNotFoundError:
        print(f"El archivo de datos no se encontró")
    except Exception as e:
        print(f"Error inesperado al leer: {e}")
        
    return filas
