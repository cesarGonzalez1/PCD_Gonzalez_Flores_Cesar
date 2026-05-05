# validadores.py
# PARTE 1: Funciones de validación individual (40%)
# Cada función valida un tipo de código con expresiones regulares
# y extrae sus componentes mediante grupos de captura.

import re
from typing import Dict
from constantes import DEPARTAMENTOS_VALIDOS, SERIES_VALIDAS


def validar_producto(codigo: str) -> Dict:
    """
    Valida código de producto y extrae componentes.
    Formato: ABC-1234-MX
      - Categoría : exactamente 3 letras MAYÚSCULAS
      - Número    : exactamente 4 dígitos
      - País      : exactamente 2 letras MAYÚSCULAS

    Patrón: ^([A-Z]{3})-([0-9]{4})-([A-Z]{2})$
      ^               inicio de cadena (no se admiten prefijos extra)
      ([A-Z]{3})      captura 3 letras mayúsculas → categoría
      -               guion literal
      ([0-9]{4})      captura exactamente 4 dígitos → número
      -               guion literal
      ([A-Z]{2})      captura 2 letras mayúsculas → país
      $               fin de cadena (no se admiten sufijos extra)
    """
    resultado = {
        "valido": False,
        "categoria": None,
        "numero": None,
        "pais": None
    }

    patron = r'^([A-Z]{3})-([0-9]{4})-([A-Z]{2})$'
    match = re.match(patron, codigo)

    if match:
        resultado["valido"] = True
        resultado["categoria"] = match.group(1)  # ej. "TEC"
        resultado["numero"] = match.group(2)       # ej. "0001"
        resultado["pais"] = match.group(3)         # ej. "MX"

    return resultado


def validar_envio(codigo: str) -> Dict:
    """
    Valida código de envío y extrae componentes.
    Formato: ENV-YYYY-MM-DD-NNNNNN
      - Prefijo     : "ENV" literal
      - Año         : 4 dígitos, rango 2020-2030
      - Mes         : 2 dígitos, rango 01-12
      - Día         : 2 dígitos, rango 01-31
      - Secuencial  : exactamente 6 dígitos

    Patrón:
      ^ENV-                              prefijo fijo
      (202[0-9]|2030)-                   año 2020-2029 ó 2030 → captura año
      (0[1-9]|1[0-2])-                   mes 01-09 ó 10-12    → captura mes
      (0[1-9]|[12][0-9]|3[01])-         día 01-31 (rangos)   → captura día
      ([0-9]{6})$                        6 dígitos secuencial → captura sec.
    """
    resultado = {
        "valido": False,
        "fecha": None,
        "secuencial": None
    }

    patron = (
        r'^ENV-'
        r'(202[0-9]|2030)-'          # año: 2020-2030
        r'(0[1-9]|1[0-2])-'          # mes: 01-12
        r'(0[1-9]|[12][0-9]|3[01])-' # día: 01-31
        r'([0-9]{6})$'                # secuencial: 6 dígitos
    )
    match = re.match(patron, codigo)

    if match:
        anio = match.group(1)
        mes  = match.group(2)
        dia  = match.group(3)
        resultado["valido"] = True
        resultado["fecha"] = f"{anio}-{mes}-{dia}"
        resultado["secuencial"] = match.group(4)

    return resultado


def validar_empleado(codigo: str) -> Dict:
    """
    Valida código de empleado y extrae componentes.
    Formato: EMP-XXX-NNNN
      - Prefijo      : "EMP" literal
      - Departamento : 3 letras MAYÚSCULAS, debe estar en DEPARTAMENTOS_VALIDOS
      - Número       : 4 dígitos, NO puede empezar con 0

    Patrón:
      ^EMP-            prefijo fijo
      ([A-Z]{3})-      captura 3 letras mayúsculas → departamento
      ([1-9][0-9]{3})$ captura número de 4 dígitos que empieza en 1-9

    La verificación del departamento válido se hace en Python
    después del match, porque la lista de departs. es dinámica.
    """
    resultado = {
        "valido": False,
        "departamento": None,
        "numero": None
    }

    # [1-9][0-9]{3}  →  primer dígito 1-9 (no cero), luego 3 dígitos cualesquiera
    patron = r'^EMP-([A-Z]{3})-([1-9][0-9]{3})$'
    match = re.match(patron, codigo)

    if match:
        depto = match.group(1)
        if depto in DEPARTAMENTOS_VALIDOS:   # verificación extra
            resultado["valido"] = True
            resultado["departamento"] = depto
            resultado["numero"] = match.group(2)

    return resultado


def validar_factura(codigo: str) -> Dict:
    """
    Valida código de factura y extrae componentes.
    Formato: FAC-S-NNNNNN
      - Prefijo : "FAC" literal
      - Serie   : una letra, debe ser A, B, C, D o E (MAYÚSCULA)
      - Número  : exactamente 6 dígitos

    Patrón:
      ^FAC-          prefijo fijo
      ([A-E])-       captura la serie (solo A-E en mayúscula) → serie
      ([0-9]{6})$    captura exactamente 6 dígitos            → número

    Nota: [A-E] ya restringe las series válidas directamente en regex,
    por lo que no es necesaria una verificación extra con SERIES_VALIDAS.
    """
    resultado = {
        "valido": False,
        "serie": None,
        "numero": None
    }

    patron = r'^FAC-([A-E])-([0-9]{6})$'
    match = re.match(patron, codigo)

    if match:
        resultado["valido"] = True
        resultado["serie"] = match.group(1)
        resultado["numero"] = match.group(2)

    return resultado
