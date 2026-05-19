import sys
import math

def main():
    datos_productos={}
    primera_linea = True

    for linea in sys.stdin:
        linea=linea.strip()

        if not linea:
            continue

        if primera_linea:
            primera_linea=False
            continue

        columnas=linea.split(",")

        if len(columnas) != 4:
            continue

        producto=columnas[1]

        try:
            cantidad=int(columnas[2])
            precio=float(columnas[3])
        except ValueError:
            continue

        if not math.isfinite(precio):
            continue

        if producto not in datos_productos:
            datos_productos[producto]={
                "unidades_vendidas": 0,
                "ingreso_total": 0.0
            }

        datos_productos[producto]["unidades_vendidas"] += cantidad
        datos_productos[producto]["ingreso_total"] += cantidad * precio

    for producto in datos_productos:
        unidades = datos_productos[producto]["unidades_vendidas"]
        ingreso = datos_productos[producto]["ingreso_total"]

        if unidades > 0:
            datos_productos[producto]["precio_promedio"] = ingreso / unidades
        else:
            datos_productos[producto]["precio_promedio"] = 0.0

    productos_ordenados = sorted(
        datos_productos.items(),
        key=lambda x: x[1]["ingreso_total"],
        reverse=True
    )

    print("producto,unidades_vendidas,ingreso_total,precio_promedio")

    for nombre, datos in productos_ordenados:
        print(f"{nombre},{datos['unidades_vendidas']},{datos['ingreso_total']:.2f},{datos['precio_promedio']:.2f}")


if __name__ == "__main__":
    main()