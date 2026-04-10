# Examen Parcial 1 - Programación para Ciencia de Datos

## Sistema de Monitoreo Meteorológico

**Matrícula:** `2025630803`
**Fecha límite de entrega:** (por definir)
**Valor:** 100 puntos

---

## Contexto

Una red de estaciones meteorológicas en la frontera usa sensores que reportan presión atmosférica en pulgadas de mercurio (inHg) y hectopascales (hPa). Necesitan unificar a hPa, clasificar lecturas por nivel de presión y generar reportes por estación del año.

---

## Datos de Entrada

El archivo `datos/lecturas_presion.csv` contiene registros con las siguientes columnas:

| Columna | Tipo esperado | Descripción |
|---------|---------------|-------------|
| `id_lectura` | texto | Código de lectura |
| `estacion` | texto | Nombre de la estación |
| `presion` | numérico (decimal) | Presión atmosférica |
| `unidad` | texto (`inHg` o `hPa`) | Unidad (inHg o hPa) |
| `temporada` | texto | Temporada del año |

**Unidades posibles:** `inHg` (Pulgadas de mercurio (inHg)) y `hPa` (Hectopascales (hPa))

**Importante:** El archivo contiene aproximadamente 1000 registros. Algunos registros
contienen errores intencionales (valores no numéricos, unidades inválidas, columnas
faltantes o sobrantes, líneas vacías). Tu programa debe manejar estos casos sin
detenerse.

### Huella de integridad de los datos

El archivo de datos proporcionado tiene el siguiente hash SHA-256:

```
dd0ab13e24b5e67bb40958bb6667645de61e6e62cf0106e7daf549948b2150bc
```

**No modifiques el archivo de datos.** Este hash se verificará automáticamente al
calificar tu examen. Si el hash no coincide, se considerará que los datos fueron
alterados y se penalizará la calificación.

> Para verificar el hash de tu archivo puedes usar:
> ```python
> import hashlib
> with open("datos/lecturas_presion.csv", "r", encoding="utf-8") as f:
>     print(hashlib.sha256(f.read().encode("utf-8")).hexdigest())
> ```

---

## Reglas de Procesamiento

### 1. Lectura del archivo
Lee el archivo CSV desde `datos/lecturas_presion.csv`. El archivo usa comas (`,`) como
separador. La primera línea es el encabezado con los nombres de las columnas.

**¿Cómo leerlo?** Abre el archivo con `open()`, lee todas las líneas, separa la
primera línea (header) del resto. Para cada línea de datos, usa `.split(",")` para
obtener los valores individuales.

### 2. Validación de cada fila
Para cada fila del archivo (después del header), verifica que sea válida. Una fila
es **inválida** y debe ignorarse si cumple cualquiera de estas condiciones:

- **Línea vacía:** la línea no contiene texto (o solo espacios en blanco)
- **Número incorrecto de columnas:** al separar por coma, no resultan exactamente
  5 valores
- **Valor no numérico:** el campo `presion` no se puede convertir a `float`
  (usa `try/except ValueError`)
- **Unidad no reconocida:** el campo `unidad` no es ni `inHg` ni `hPa`
  (la comparación es sensible a mayúsculas/minúsculas)

**Importante:** Tu programa no debe detenerse ni mostrar errores cuando encuentre
filas inválidas; simplemente las ignora y continúa con la siguiente.

### 3. Conversión de unidades
Para los registros válidos, convierte los valores que están en `inHg` a `hPa`
usando la fórmula:

```
hPa = inHg × 33.8639
```

En Python:
```python
hpa = inhg * 33.8639
```

Los valores que **ya están en `hPa`** se mantienen sin cambio alguno.

Después de la conversión, redondea el resultado a **1 decimal**
usando la función `round()`.

### 4. Clasificación
Clasifica cada registro según el valor **ya convertido** a `hPa`:

| Categoría | Rango (hPa) | Regla |
|-----------|------|-------|
| Muy baja | < 997.2 | `valor < 997.2` |
| Baja | 997.2 - 1010.4 | `997.2 <= valor < 1010.4` |
| Normal | 1010.4 - 1021.1 | `1010.4 <= valor < 1021.1` |
| Alta | 1021.1 - 1032.0 | `1021.1 <= valor < 1032.0` |
| Muy alta | >= 1032.0 | `valor >= 1032.0` |


> **Convención de límites:** Los límites inferiores son **inclusivos** (`>=`) y los
> superiores son **exclusivos** (`<`), excepto en la última categoría donde solo hay
> límite inferior inclusivo.

### 5. Generación de archivos de salida

Tu programa debe generar **dos archivos CSV** en la carpeta `salidas/`. A continuación
se describe cada uno en detalle.

---

## Archivo de Salida 1: `salidas/reporte_detalle.csv`

Este archivo contiene **un registro por cada fila válida** del archivo de entrada,
con el valor ya convertido y su clasificación.

### Columnas del archivo

| # | Columna | Tipo | Descripción | Ejemplo |
|---|---------|------|-------------|---------|
| 1 | `id_lectura` | texto | ID original, copiado tal cual de la entrada | `LEC-0001` |
| 2 | `estacion` | texto | Nombre original, copiado tal cual de la entrada | (varía) |
| 3 | `temporada` | texto | Grupo/categoría original | (varía) |
| 4 | `presion_hpa` | decimal | Valor convertido a hPa, con 1 decimal | `37.5` |
| 5 | `nivel_presion` | texto | Clasificación asignada según los umbrales | (varía) |

### Reglas del archivo
- **Primera línea (header):** `id_lectura,estacion,temporada,presion_hpa,nivel_presion`
- **Ordenamiento:** ascendente por `id_lectura` (orden alfabético/numérico del ID)
- **Separador:** coma (`,`), sin espacios alrededor
- **Decimales:** los valores en `presion_hpa` deben tener exactamente
  1 decimal (usa f-string: `f"{valor:.1f}"`)
- **Sin filas inválidas:** solo aparecen registros que pasaron la validación

### Cómo generarlo paso a paso
1. Filtra solo los registros válidos (los que pasaron la validación del paso 2)
2. Para cada registro: convierte el valor (paso 3), clasifícalo (paso 4)
3. Almacena los resultados en una lista
4. Ordena la lista por ID ascendente
5. Escribe el header seguido de cada registro, una línea por registro

---

## Archivo de Salida 2: `salidas/reporte_resumen.csv`

Este archivo contiene **una fila por cada grupo** (`temporada`), con métricas
agregadas calculadas a partir de los registros válidos.

### Columnas del archivo

| # | Columna | Tipo | Descripción | Cómo calcularlo |
|---|---------|------|-------------|-----------------|
| 1 | `temporada` | texto | Nombre del grupo | La clave del diccionario de agrupación |
| 2 | `conteo` | entero | Cantidad de registros válidos en ese grupo | Contar cuántos registros pertenecen al grupo |
| 3 | `promedio` | decimal | Promedio del valor convertido, 1 decimal | Suma de valores / conteo |
| 4 | `maximo` | decimal | Valor máximo convertido, 1 decimal | El mayor valor del grupo |

### Reglas del archivo
- **Primera línea (header):** `temporada,conteo,promedio,maximo`
- **Ordenamiento principal:** descendente por `conteo` (el grupo con más registros primero)
- **Desempate:** si dos grupos tienen el mismo conteo, orden alfabético por `temporada`
- **Decimales:** `promedio` y `maximo` con exactamente 1 decimal
- **`conteo`** es un entero (sin decimales)

### Cómo generarlo paso a paso
1. Usa un **diccionario** para agrupar: la clave es el valor de `temporada`, el valor
   es otro diccionario con `conteo`, `suma` y `maximo`
2. Recorre todos los registros válidos (ya procesados en el detalle):
   - Si el grupo no existe en el diccionario, créalo con conteo=0, suma=0.0, maximo=-infinito
   - Incrementa el conteo, suma el valor convertido, actualiza el máximo si corresponde
3. Calcula el promedio: `promedio = suma / conteo`
4. Ordena por conteo descendente (y alfabético en caso de empate)
5. Escribe el header seguido de cada grupo

---

## Estructura del Proyecto Requerida

```
examen_2025630803/
├── main.py                    # Punto de entrada: orquesta todo el proceso
├── models/
│   ├── __init__.py            # Puede estar vacío o exportar la clase
│   └── lectura.py        # Definición de la clase Lectura
├── utils/
│   ├── __init__.py            # Puede estar vacío o exportar funciones
│   ├── io_helpers.py          # Funciones para leer CSV y escribir reportes
│   └── validators.py          # Funciones para validar filas del CSV
├── datos/
│   └── lecturas_presion.csv      # Archivo de entrada (proporcionado, NO modificar)
└── salidas/
    ├── reporte_detalle.csv    # Generado por tu programa
    └── reporte_resumen.csv    # Generado por tu programa
```

### Descripción de cada archivo

**`main.py`** — Punto de entrada. Al ejecutar `python main.py` desde la raíz del
proyecto, debe:
1. Leer el archivo de datos usando funciones de `utils/io_helpers.py`
2. Validar cada fila usando funciones de `utils/validators.py`
3. Crear objetos `Lectura` para cada registro válido
4. Generar el reporte de detalle y escribirlo en `salidas/reporte_detalle.csv`
5. Generar el reporte de resumen y escribirlo en `salidas/reporte_resumen.csv`

**`models/lectura.py`** — Contiene la clase `Lectura` (ver sección siguiente).

**`utils/io_helpers.py`** — Contiene al menos:
- Una función para **leer** el archivo CSV y retornar las filas como lista de listas o diccionarios
- Una función para **escribir** un archivo CSV a partir de una lista de datos

**`utils/validators.py`** — Contiene al menos:
- Una función para **validar** si una fila del CSV es válida (número correcto de
  columnas, valor numérico, unidad reconocida)
- Debe retornar `True`/`False` o una tupla `(es_valido, mensaje_error)`

---

## Clase Requerida: `Lectura`

La clase `Lectura` en `models/lectura.py` debe incluir:

- **`__init__(self, ...)`**: Recibe y almacena como atributos: `id_lectura`,
  `estacion`, el valor ya convertido a hPa, y `temporada`
- **`clasificar(self)`**: Método que retorna un string con la clasificación según
  los umbrales definidos (ej: `"Muy baja"`, `"Baja"`, etc.)
- **`__str__(self)`**: Retorna una representación legible para el usuario
  (ej: `"LEC-0001 - NombreEjemplo (temporada: GrupoEjemplo) - 37.5 hPa"`)
- **`__repr__(self)`**: Retorna una representación técnica para depuración
  (ej: `"Lectura(id='LEC-0001', valor=37.5, clase='Normal')"`)

---

## Ejemplo

### Entrada (primeras filas de `datos/lecturas_presion.csv`):
```csv
id_lectura,estacion,presion,unidad,temporada
LEC-0001,Est. Sierra,30.8,inHg,Verano
LEC-0002,Est. Centro,971.5,?,Canícula
LEC-0003,Est. Planicie,1007.61,hPa,Otoño
LEC-0004,Est. Sur,1003.81,hPa,Transición Primavera-Verano
LEC-0005,Est. Planicie,30.42,inHg,Primavera
```

### Salida detalle esperada (`salidas/reporte_detalle.csv`):
```csv
id_lectura,estacion,temporada,presion_hpa,nivel_presion
LEC-0001,Est. Sierra,Verano,1043.0,Muy alta
LEC-0003,Est. Planicie,Otoño,1007.6,Baja
LEC-0004,Est. Sur,Transición Primavera-Verano,1003.8,Baja
LEC-0005,Est. Planicie,Primavera,1030.1,Alta
LEC-0006,Est. Poniente,Temporada de lluvias,1049.4,Muy alta
```

### Salida resumen esperada (`salidas/reporte_resumen.csv`):
```csv
temporada,conteo,promedio,maximo
Transición Otoño-Invierno,137,1007.8,1049.8
Otoño,127,1007.4,1049.7
Verano,115,1006.7,1047.1
Primavera,113,1008.8,1048.6
Invierno,111,1009.6,1049.4
```

---

## Criterios de Evaluación

| Criterio | Puntos | Detalle |
|----------|--------|---------|
| Estructura del proyecto | 15 | Carpetas, archivos, `__init__.py`, imports correctos |
| Clase `Lectura` | 20 | `__init__`, `clasificar()`, `__str__`, `__repr__` |
| Validación de datos | 10 | Manejo correcto de filas inválidas |
| Conversión de unidades | 15 | Fórmula correcta, precisión decimal |
| Clasificación | 10 | Umbrales correctos, categorías asignadas |
| Agrupación y métricas | 15 | Conteo, promedio, máximo por grupo |
| Formato de salida | 10 | CSVs con columnas, orden y formato correctos |
| Git | 5 | Mínimo 5 commits descriptivos, `.gitignore` |
| **Total** | **100** | |

> **Nota:** Se verificará automáticamente que el hash SHA-256 del archivo de datos
> coincida con `dd0ab13e24b5e67bb40958bb6667645de61e6e62cf0106e7daf549948b2150bc`. Si el archivo fue modificado, se aplicará una
> penalización.

---

## Instrucciones de Entrega

1. Crea un repositorio en GitHub llamado `examen1_pcd`
2. Desarrolla tu solución siguiendo la estructura indicada
3. Asegúrate de que tu programa funciona ejecutando: `python main.py`
4. Tu programa debe leer de `datos/lecturas_presion.csv` y escribir en `salidas/`
5. Haz **mínimo 5 commits** con mensajes descriptivos
6. Incluye un `.gitignore` apropiado
7. **NO modifiques** el archivo `datos/lecturas_presion.csv` (se verificará su integridad)
8. Entrega el enlace a tu repositorio antes de la fecha límite

## Restricciones

- **NO** uses pandas, numpy ni librerías externas (solo biblioteca estándar de Python)
- **NO** copies código de otros compañeros (cada examen tiene datos y umbrales únicos)
- **NO** modifiques el archivo de datos proporcionado
- Tu código debe funcionar con **cualquier** archivo que siga el formato descrito,
  no solo con los datos proporcionados
