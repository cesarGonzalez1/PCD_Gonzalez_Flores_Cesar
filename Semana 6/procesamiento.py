
from typing import Dict, List
from validador_universal import validar_codigo


def procesar_lote(codigos: List[str]) -> Dict:
    """
    Procesa múltiples códigos y genera estadísticas.

    Algoritmo:
      Para cada código en la lista:
        1. Llama a validar_codigo() para obtener tipo y resultado.
        2. Incrementa los contadores globales (total, validos, invalidos).
        3. Incrementa los contadores del sub-dict 'por_tipo' según el tipo.
        4. Agrega el resultado completo al detalle.

    Retorna:
        {
            "total"   : int,
            "validos" : int,
            "invalidos": int,
            "por_tipo": {
                "producto"    : {"total": int, "validos": int},
                "envio"       : {"total": int, "validos": int},
                "empleado"    : {"total": int, "validos": int},
                "factura"     : {"total": int, "validos": int},
                "desconocido" : {"total": int, "validos": int},
            },
            "detalle" : [lista de dicts devueltos por validar_codigo]
        }
    """
    resultado = {
        "total": 0,
        "validos": 0,
        "invalidos": 0,
        "por_tipo": {
            "producto":    {"total": 0, "validos": 0},
            "envio":       {"total": 0, "validos": 0},
            "empleado":    {"total": 0, "validos": 0},
            "factura":     {"total": 0, "validos": 0},
            "desconocido": {"total": 0, "validos": 0},
        },
        "detalle": []
    }

    for codigo in codigos:
        validacion = validar_codigo(codigo)
        tipo = validacion["tipo"]
        es_valido = validacion["valido"]

        resultado["total"] += 1
        if es_valido:
            resultado["validos"] += 1
        else:
            resultado["invalidos"] += 1

        resultado["por_tipo"][tipo]["total"] += 1
        if es_valido:
            resultado["por_tipo"][tipo]["validos"] += 1

        resultado["detalle"].append(validacion)

    return resultado
