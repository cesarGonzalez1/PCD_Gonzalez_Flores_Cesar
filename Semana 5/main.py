import argparse
import sys

def es_valor_nulo(valor):
    """Determina si un valor se considera nulo."""
    if valor is None:
        return True
    if isinstance(valor, str) and valor.strip() == "":
        return True
    return False

def es_numerico(valor):
    """Verifica si un valor es numérico."""
    try:
        float(str(valor).replace(',', '').strip())
        return True
    except (ValueError, TypeError):
        return False

def es_fecha(valor):
    """Verifica si un valor parece una fecha YYYY-MM-DD."""
    v = str(valor).strip()
    if len(v) >= 10 and v[4] == '-' and v[7] == '-':
        try:
            partes = v[:10].split('-')
            año, mes, dia = int(partes[0]), int(partes[1]), int(partes[2])
            return 1900 <= año <= 2100 and 1 <= mes <= 12 and 1 <= dia <= 31
        except (ValueError, IndexError):
            pass
    return False

def es_booleano(valor):
    """Verifica si un valor es booleano."""
    v = str(valor).strip().lower()
    return v in ['true', 'false', 'yes', 'no', 'si', '1', '0', 't', 'f']