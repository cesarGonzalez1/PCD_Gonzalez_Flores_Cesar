import sys

def main():

    print("ciudad,temperatura_celsius,clasificacion")
    
    primera_linea = True
    
    for linea in sys.stdin:
        if primera_linea:
            primera_linea = False
            continue
            
        partes = linea.strip().split(',')
        ciudad, temp_val, unidad = partes[0], float(partes[1]), partes[2].upper()

        celsius = (temp_val - 32) * 5 / 9 if unidad == 'F' else temp_val
        
        if celsius < 0: cat = "Congelante"
        elif celsius <= 15: cat = "Frio"
        else: cat = "Otro"
        
        print(f"{ciudad},{celsius:.1f},{cat}")

if __name__ == "__main__":
    main()