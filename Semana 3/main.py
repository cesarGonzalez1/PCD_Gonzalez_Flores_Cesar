import sys

def main():
    
    productos = {}
    primera_linea = True

    for linea in sys.stdin:
        linea = linea.strip()

        if primera_linea:
            primera_linea = False
            continue

        if not linea:
            continue

        partes = linea.split(',')
        if len(partes) != 4:
            continue

        nombre_prod = partes[1]

        try:
            cant = int(partes[2])
            valor = float(partes[3])
        except:
            continue

        info = productos.get(nombre_prod)
        if info is None:
            productos[nombre_prod] = {
                "unidades": cant,
                "ingreso": cant * valor
            }
        else:
            info["unidades"] = info["unidades"] + cant
            info["ingreso"] = info["ingreso"] + (cant * valor)

    for clave, info in productos.items():
        total_u = info["unidades"]
        total_ing = info["ingreso"]

        info["promedio"] = (total_ing / total_u) if total_u != 0 else 0

    lista_ordenada = sorted(
        productos.items(),
        key=lambda elemento: elemento[1]["ingreso"],
        reverse=True
    )

    encabezado = "producto,unidades_vendidas,ingreso_total,precio_promedio"
    print(encabezado)

    for prod, info in lista_ordenada:
        unidades = info["unidades"]
        ingreso = info["ingreso"]
        promedio = info["promedio"]

        print(f"{prod},{unidades},{ingreso:.2f},{promedio:.2f}")


if __name__ == "__main__":
    main()