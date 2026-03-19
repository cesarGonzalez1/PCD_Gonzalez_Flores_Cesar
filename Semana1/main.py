import sys


def limpiar_valor(valor):
    """
    Limpia un valor individual:
    - Quita espacios
    - Elimina caracteres no válidos
    - Retorna el número limpio como string
    """
    valor = valor.strip()
    caracteres_validos = "0123456789.-"
    limpio = ""

    for char in valor:
        if char in caracteres_validos:
            limpio += char

    return limpio


def convertir_a_entero(texto):
    """
    Convierte texto a entero truncando decimales.
    Si no es convertible, retorna 0.
    """
    if not texto:
        return 0

    try:
        numero = float(texto)
        return int(numero)  # Trunca hacia cero
    except ValueError:
        return 0


def procesar_linea(linea):
    """
    Procesa una línea completa:
    - Si está vacía -> 0
    - Separa por comas
    - Limpia cada valor
    - Convierte a entero truncado
    - Suma todos los valores
    """
    linea = linea.strip()

    # Regla 1: línea vacía
    if not linea:
        return 0

    valores = linea.split(",")
    suma = 0

    for valor in valores:
        limpio = limpiar_valor(valor)
        numero = convertir_a_entero(limpio)
        suma += numero

    return suma


def main():
    for linea in sys.stdin:
        resultado = procesar_linea(linea)
        print(resultado)


if __name__ == "__main__":
    main()