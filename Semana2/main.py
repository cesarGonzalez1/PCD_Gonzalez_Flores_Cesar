import sys

def fahrenheit_a_celsius(f):
    """Aplica la fórmula estándar de conversión."""
    return (f - 32) * 5 / 9

def clasificar_temperatura(celsius):
    """Clasifica según los rangos estrictos del IPN."""
    if celsius < 0:
        return "Congelante"
    elif 0 <= celsius <= 15:
        return "Frio"
    elif 16 <= celsius <= 25:
        return "Templado"
    elif 26 <= celsius <= 35:
        return "Calido"
    else: # > 35
        return "Extremo"

def main():
    print("ciudad,temperatura_celsius,clasificacion")
    
    primera_linea = True
    for linea in sys.stdin:
        linea = linea.strip()
        
        if not linea or primera_linea:
            primera_linea = False
            continue
            
        partes = linea.split(',')
        
        if len(partes) != 3:
            continue
            
        ciudad = partes[0].strip()
        temp_str = partes[1].strip()
        unidad = partes[2].strip().upper()
        
        try:
            temp_valor = float(temp_str)
            if unidad not in ['C', 'F']:
                continue
        except ValueError:
            continue 
            
        celsius = fahrenheit_a_celsius(temp_valor) if unidad == 'F' else temp_valor
        
        categoria = clasificar_temperatura(celsius)
        
        print(f"{ciudad},{celsius:.1f},{categoria}")

if __name__ == "__main__":
    main()