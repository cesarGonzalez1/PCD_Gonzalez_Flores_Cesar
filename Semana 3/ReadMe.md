

Este proyecto procesa un archivo CSV con transacciones de ventas y genera un **reporte consolidado por producto**, mostrando:

* Unidades vendidas
* Ingreso total
* Precio promedio

El resultado se ordena de **mayor a menor ingreso**.



## Formato de Entrada

Archivo CSV leído desde `stdin` con la siguiente estructura:

```
fecha,producto,cantidad,precio_unitario
2026-01-01,Laptop,2,15000.00
2026-01-02,Mouse,10,250.00
```

---

##  Formato de Salida

CSV generado en `stdout`:

```
producto,unidades_vendidas,ingreso_total,precio_promedio
Laptop,3,44500.00,14833.33
Mouse,18,4500.00,250.00
```

---

##  Cómo ejecutar usando archivo de entrada 

```
python main.py < entrada.txt > salida.txt
```



##  Estructura del Proyecto

```
reto-semana-03/
├── main.py
├── README.md
├── tests/
│   ├── entrada1.txt
│   └── salida1.txt
```

---

##  Lógica de Solución

1. Leer datos desde `stdin`
2. Ignorar encabezado
3. Validar datos
4. Agrupar por producto usando diccionario
5. Calcular:

   * Unidades totales
   * Ingreso total
   * Precio promedio
6. Ordenar por ingreso descendente
7. Imprimir resultado en formato CSV

---

##  Manejo de Errores

Se ignoran líneas que:

* No tengan 4 columnas
* Tengan valores no numéricos en cantidad o precio

---

##  Tecnologías

* Python 3
* Diccionarios
* Manejo de archivos (stdin / stdout)

---
