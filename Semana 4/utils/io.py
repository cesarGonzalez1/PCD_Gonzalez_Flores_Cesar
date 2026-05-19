import csv
import os


def leer_inventario(ruta_archivo):
    """
    Lee el inventario desde un archivo CSV.

    Returns:
        list[dict]: Lista de filas como diccionarios, o lista vacía si falla.
    """
    # BUG FIX: manejo de errores si el archivo no existe
    if not os.path.exists(ruta_archivo):
        print(f"Error: No se encontro el archivo '{ruta_archivo}'.")
        return []

    productos_raw = []

    try:
        # BUG FIX: usar csv.reader en lugar de split(',')
        # para manejar correctamente campos con comas internas
        with open(ruta_archivo, 'r', encoding='utf-8-sig') as archivo:
            reader = csv.DictReader(archivo)
            for fila in reader:
                # Ignorar filas completamente vacías
                if any(v.strip() for v in fila.values() if v):
                    productos_raw.append(dict(fila))
    except OSError as e:
        print(f"Error al leer '{ruta_archivo}': {e}")

    return productos_raw


def escribir_reporte(productos, ruta):
    """
    Escribe el reporte de productos en reorden a un archivo CSV.
    """
    # BUG FIX: crear directorio de salida si no existe
    directorio = os.path.dirname(ruta)
    if directorio:
        os.makedirs(directorio, exist_ok=True)

    try:
        # BUG FIX: usar csv.writer para manejar comas en campos correctamente
        with open(ruta, "w", encoding="utf-8", newline="") as archivo:
            campos = ["sku", "nombre", "categoria", "stock_actual",
                      "stock_minimo", "unidades_faltantes", "valor_inventario"]
            writer = csv.DictWriter(archivo, fieldnames=campos)
            writer.writeheader()

            for p in productos:
                writer.writerow({
                    "sku": p.sku,
                    "nombre": p.nombre,
                    "categoria": p.categoria,
                    "stock_actual": p.stock,
                    "stock_minimo": p.stock_minimo,
                    "unidades_faltantes": p.unidades_faltantes(),
                    "valor_inventario": f"{p.valor_inventario():.2f}"
                })
    except OSError as e:
        print(f"Error al escribir '{ruta}': {e}")
