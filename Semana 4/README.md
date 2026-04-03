# Reto Semana 4: Sistema de Inventario Modular
Se implementa un sistema automatizado para el departamento de compras de una cadena de tiendas de tecnología. El sistema lee un inventario actual, evalúa los niveles de existencia contra los mínimos requeridos y genera un reporte detallado con los productos que necesitan ser reordenados, priorizando aquellos con mayor urgencia (unidades faltantes).

##  Características Principales

* **Lectura de datos estructurada:** Ingesta de datos desde formato CSV.
* **Validación robusta:** Manejo silencioso de errores (ignora líneas inválidas, precios nulos o stock con formato incorrecto) sin interrumpir la ejecución.
* **Lógica orientada a objetos:** Uso de la clase `Producto` para encapsular atributos y calcular métodos dinámicos como `unidades_faltantes()` y `valor_inventario()`.
* **Generación de reportes:** Salida automatizada en CSV, ordenada de mayor a menor urgencia de reabastecimiento.

##  Estructura del Proyecto

El código está organizado bajo un enfoque modular para facilitar su mantenimiento y escalabilidad:

```text
reto_semana_04/
│
├── main.py                    # Script orquestador y punto de entrada
├── README.md                  # Documentación del proyecto
├── .gitignore                 # Archivos y carpetas a ignorar en Git
│
├── models/                    # Lógica de dominio
│   ├── __init__.py
│   └── producto.py            # Definición de la clase Producto
│
├── utils/                     # Módulos de soporte
│   ├── __init__.py
│   ├── io.py                  # Funciones de lectura y escritura de CSV
│   └── validators.py          # Validaciones de integridad de datos
│
├── data/                      # Directorio de entradas
│   └── inventario.csv         # Archivo de inventario inicial (fuente)
│
└── outputs/                   # Directorio de salidas
    └── reporte_inventario.csv # Archivo generado por el sistema
```
##  Entrada
El sistema procesa el archivo localizado en `data/inventario.csv`. 

**Formato de datos:**
El archivo es un CSV (valores separados por comas) con los siguientes campos:
* `sku`: Texto (Identificador único).
* `nombre`: Texto (Nombre comercial).
* `categoria`: Texto (Categoría del producto).
* `precio`: Decimal (Precio unitario).
* `stock`: Entero (Existencia actual).
* `stock_minimo`: Entero (Nivel crítico de inventario).

> **Nota:** El sistema ignora automáticamente líneas con datos no numéricos en campos de precio/stock o con número de columnas incorrecto.

##  Salida
El reporte generado se ubica en `outputs/reporte_inventario.csv` e incluye **solo** los productos donde `stock < stock_minimo`.

**Formato del reporte:**
* `sku`: Identificador.
* `nombre`: Nombre del producto.
* `categoria`: Categoría.
* `stock_actual`: Cantidad en bodega.
* `stock_minimo`: Mínimo requerido.
* `unidades_faltantes`: Cálculo de `stock_minimo - stock`.
* `valor_inventario`: Cálculo de `precio * stock`.

## Como Ejecutar

```bash
python main.py
```
## Autor
Gonzalez Flores Cesar