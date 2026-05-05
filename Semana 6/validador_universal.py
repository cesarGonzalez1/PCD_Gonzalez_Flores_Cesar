
from typing import Dict
from validadores import (
    validar_producto,
    validar_envio,
    validar_empleado,
    validar_factura,
)


_DISPATCH = {
    "ENV": ("envio",    validar_envio),
    "EMP": ("empleado", validar_empleado),
    "FAC": ("factura",  validar_factura),
}


def validar_codigo(codigo: str) -> Dict:
    """
    Detecta el tipo de código y lo valida automáticamente.

    Estrategia de detección:
      1. Se obtiene el prefijo: todo lo que está antes del primer '-'.
      2. Si el prefijo está en _DISPATCH → se usa la función asociada.
      3. Si el prefijo tiene exactamente 3 letras mayúsculas y NO está
         en _DISPATCH → se intenta validar como 'producto' (formato ABC-…).
      4. Cualquier otro caso → tipo 'desconocido'.

    Retorna:
        {
            "codigo"  : str,   # código original tal como llegó
            "tipo"    : str,   # producto / envio / empleado / factura / desconocido
            "valido"  : bool,
            "detalles": dict   # componentes extraídos si es válido, {} si no
        }
    """
    resultado = {
        "codigo": codigo,
        "tipo": "desconocido",
        "valido": False,
        "detalles": {}
    }

    partes = codigo.split("-", 1)
    prefijo = partes[0]

    if prefijo in _DISPATCH:
        tipo, fn = _DISPATCH[prefijo]
        resultado["tipo"] = tipo
        validacion = fn(codigo)

    elif len(codigo.split("-")) == 3:
        resultado["tipo"] = "producto"
        validacion = validar_producto(codigo)

    else:
        return resultado

    resultado["valido"] = validacion["valido"]
    if validacion["valido"]:
        resultado["detalles"] = {
            k: v for k, v in validacion.items() if k != "valido"
        }

    return resultado
