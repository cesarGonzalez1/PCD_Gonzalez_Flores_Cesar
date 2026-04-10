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

def escribir_csv(ruta, datos):
    directorio = os.path.dirname(ruta)
    if directorio and not os.path.exists(directorio):
        os.makedirs(directorio)
    try:
        with open(ruta, 'w', encoding='utf-8') as f:
            for fila in datos:
              
                linea = ",".join(str(elemento) for elemento in fila)
                f.write(linea + "\n")
    except Exception as e:
        print(f"Error al escribir el reporte en {ruta}: {e}")