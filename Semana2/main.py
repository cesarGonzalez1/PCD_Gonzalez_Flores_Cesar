import sys

def main():

    print("ciudad,temperatura_celsius,clasificacion")
    
    for linea in sys.stdin:
       
        partes = linea.strip().split(',')
        if len(partes) == 3:
            ciudad = partes[0]
            print(f"{ciudad},0.0,Pendiente")

if __name__ == "__main__":
    main()