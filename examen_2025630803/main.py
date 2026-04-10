import os
from models.lectura import Lectura
from utils.io_helpers import leer_csv, escribir_csv
from utils.validators import es_filaval

def convertir_a_hpa(valor, unidad):
   
    if unidad == 'inHg':
        hpa = valor * 33.8639
        return round(hpa, 1)
    return round(valor, 1)

def main():
    ruta_entrada = os.path.join("datos", "lecturas_presion.csv")
    ruta_detalle = os.path.join("salidas", "reporte_detalle.csv")
    ruta_resumen = os.path.join("salidas", "reporte_resumen.csv")