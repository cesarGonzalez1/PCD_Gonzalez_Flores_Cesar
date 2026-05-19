
from models.producto import Producto
from utils.validators import validar_producto
from utils.io import leer_inventario, escribir_reporte

# Configuracion
ARCHIVO_INVENTARIO = "data/inventario.csv"
ARCHIVO_REPORTE = "outputs/reporte_inventario.csv"


def crear_productos(datos_raw):
    
    productos = []
    
    for datos in datos_raw:
        # Validar
        es_valido, error = validar_producto(
            datos.get('sku'),
            datos.get('nombre'),
            datos.get('categoria'),
            datos.get('precio'),
            datos.get('stock'),
            datos.get('stock_minimo')
        )
        
        if not es_valido:
            print(f"Advertencia: Ignorando registro invalido - {error}")
            continue
        
        # Crear objeto Producto
        producto = Producto(
            sku=datos['sku'],
            nombre=datos['nombre'],
            categoria=datos['categoria'],
            precio=float(datos['precio']),
            stock=int(datos['stock']),
            stock_minimo=int(datos['stock_minimo'])
        )
        productos.append(producto)
    
    return productos


def filtrar_necesitan_reorden(productos):
    """Filtra productos que necesitan reorden."""
    return [p for p in productos if p.necesita_reorden()]


def ordenar_por_faltantes(productos):
    """Ordena por unidades faltantes (descendente)."""
    return sorted(productos, key=lambda p: p.unidades_faltantes(), reverse=True)


def main():

    datos = leer_inventario(ARCHIVO_INVENTARIO)

    productos = crear_productos(datos)

    reorden = filtrar_necesitan_reorden(productos)

    reorden = ordenar_por_faltantes(reorden)

    for p in reorden:
        print(p)

    escribir_reporte(reorden, ARCHIVO_REPORTE)

if __name__ == "__main__":
    main()