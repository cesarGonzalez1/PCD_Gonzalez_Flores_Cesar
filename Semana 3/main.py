import sys
import csv
import io

def main():
    raw_data = sys.stdin.buffer.read()
    
    if not raw_data:
        return

    try:
        if b'\x00' in raw_data:
            contenido = raw_data.decode('utf-16')
        else:
            contenido = raw_data.decode('utf-8-sig')
    except UnicodeDecodeError:
        contenido = raw_data.decode('latin-1')

    f = io.StringIO(contenido.strip())
    reader = csv.reader(f)
    
    productos = {}
    
    try:
        next(reader)
    except StopIteration:
        return

    for fila in reader:
        fila = [col.strip() for col in fila if col.strip()]
        
        if len(fila) < 4:
            continue

        try:
            nombre_prod = fila[1]
            cant = int(fila[2])
            valor = float(fila[3])
            
            if nombre_prod not in productos:
                productos[nombre_prod] = {"u": 0, "i": 0.0}
            
            productos[nombre_prod]["u"] += cant
            productos[nombre_prod]["i"] += (cant * valor)
            
        except (ValueError, IndexError):
            continue

    print("producto,unidades_vendidas,income_total,precio_promedio")
    
    if not productos:
        return

    resultados = []
    for nombre, datos in productos.items():
        u = datos["u"]
        ing = datos["i"]
        prom = ing / u if u > 0 else 0
        resultados.append((nombre, u, ing, prom))

    resultados.sort(key=lambda x: x[2], reverse=True)

    for nombre, u, ing, prom in resultados:
        print(f"{nombre},{u},{ing:.2f},{prom:.2f}")

if __name__ == "__main__":
    main()