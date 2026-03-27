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
