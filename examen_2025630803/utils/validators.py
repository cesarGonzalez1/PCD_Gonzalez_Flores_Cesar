def es_filaval(fila):
   
    if len(fila) != 5:
        return False
    
    presion_str = fila[2].strip()
    unidad = fila[3].strip()
    try:
        float(presion_str)
    except ValueError:
        return False
    
    if unidad not in ['inHg', 'hPa']:
        return False
    
    return True