# bonus.py
# BONUS: Funcionalidades Extra (+10 puntos)

import csv
import re
from datetime import date
from typing import Dict


def sugerir_correccion(codigo: str) -> str:
    """
    Sugiere una corrección para códigos inválidos cuando el error es
    menor (solo de formato, no de contenido).

    Reglas aplicadas (en orden):
      a) Si hay letras minúsculas → convertir todo a mayúsculas.
      b) Si después de convertir el código ya es válido, se devuelve.
      c) Cualquier otro tipo de error estructural devuelve el original
         con una nota indicando que no se pudo corregir automáticamente.

    Ejemplos:
      "tec-0001-MX"   → "TEC-0001-MX"
      "fac-a-123456"  → "FAC-A-123456"
      "TEC-001-MX"    → "TEC-001-MX  (sin corrección automática)"
    """
    from validador_universal import validar_codigo  
    if validar_codigo(codigo)["valido"]:
        return codigo

    sugerencia = codigo.upper()
    if validar_codigo(sugerencia)["valido"]:
        return sugerencia

    sugerencia = codigo.strip().upper()
    if validar_codigo(sugerencia)["valido"]:
        return sugerencia

    return f"{codigo}  (sin corrección automática)"



def validar_fecha_real(anio: int, mes: int, dia: int) -> bool:
    """
    Valida que una fecha sea real usando el módulo datetime.
    Esto captura casos como febrero 30, abril 31, etc.

    Retorna True si la fecha existe en el calendario, False en caso contrario.

    Ejemplos:
      validar_fecha_real(2024, 2, 29) → True  (2024 es bisiesto)
      validar_fecha_real(2023, 2, 29) → False (2023 NO es bisiesto)
      validar_fecha_real(2024, 4, 31) → False (abril tiene 30 días)
    """
    try:
        date(anio, mes, dia)
        return True
    except ValueError:
        return False

def exportar_resultados(reporte: Dict, archivo: str) -> None:
    """
    Guarda el detalle de validación del reporte en un archivo CSV.

    Columnas generadas:
      codigo, tipo, valido, detalles

    El campo 'detalles' se serializa como pares clave=valor separados por ';'
    para mantener el CSV legible sin columnas variables.

    Ejemplo de fila:
      TEC-0001-MX, producto, True, categoria=TEC;numero=0001;pais=MX
    """
    detalle = reporte.get("detalle", [])
    if not detalle:
        print("El reporte no contiene detalle de códigos.")
        return

    campos = ["codigo", "tipo", "valido", "detalles"]

    with open(archivo, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()

        for entrada in detalle:
            detalles_str = ";".join(
                f"{k}={v}" for k, v in entrada.get("detalles", {}).items() if v is not None
            )
            writer.writerow({
                "codigo":   entrada["codigo"],
                "tipo":     entrada["tipo"],
                "valido":   entrada["valido"],
                "detalles": detalles_str,
            })

    print(f"Resultados exportados a: {archivo}")
