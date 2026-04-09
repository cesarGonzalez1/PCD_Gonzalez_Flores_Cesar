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
def inferir_tipo(valores):
    """Infiere el tipo de una columna."""
    valores_validos = [v for v in valores if not es_valor_nulo(v)]
    
    if not valores_validos:
        return "texto"
        
    total = len(valores_validos)
    umbral = 0.8
    
    num_fechas = sum(1 for v in valores_validos if es_fecha(v))
    num_booleanos = sum(1 for v in valores_validos if es_booleano(v))
    num_numericos = sum(1 for v in valores_validos if es_numerico(v))
    
    if num_fechas / total >= umbral:
        return "fecha"
    elif num_booleanos / total >= umbral:
        return "booleano"
    elif num_numericos / total >= umbral:
        return "numerico"
    else:
        return "texto"

def perfilar_columna(nombre, valores):
    """Genera el perfil de una columna."""
    total = len(valores)
    nulos = sum(1 for v in valores if es_valor_nulo(v))
    valores_no_nulos = [v for v in valores if not es_valor_nulo(v)]
    unicos = len(set(valores_no_nulos))
    ejemplo = valores_no_nulos[0] if valores_no_nulos else ""
    tipo = inferir_tipo(valores)
    
    pct_nulos = round(nulos / total * 100, 2) if total > 0 else 0.00
    pct_unicos = round(unicos / total * 100, 2) if total > 0 else 0.00
    
    return {
        "nombre_columna": nombre,
        "tipo_inferido": tipo,
        "total_registros": total,
        "valores_nulos": nulos,
        "porcentaje_nulos": pct_nulos,
        "valores_unicos": unicos,
        "porcentaje_unicos": pct_unicos,
        "ejemplo_valor": ejemplo
    }

def leer_csv(ruta):
    """Lee un archivo CSV y retorna encabezados y filas."""
    with open(ruta, 'r', encoding='utf-8') as f:
        lineas = f.readlines()
        
    if not lineas:
        return [], []
        
    encabezados = lineas[0].strip().split(',')
    filas = [linea.strip().split(',') for linea in lineas[1:] if linea.strip()]
    
    return encabezados, filas