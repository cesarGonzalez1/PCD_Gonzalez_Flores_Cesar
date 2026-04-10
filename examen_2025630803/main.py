import os
from models.lectura import Lectura
from utils.io_helpers import leer_csv, escribir_csv
from utils.validators import es_filaval

def convertir_a_hpa(valor, unidad):
   
    if unidad == 'inHg':
        hpa = valor * 33.8639
        return round(hpa, 1)
    return round(valor, 1)

def main():
    ruta_entrada = os.path.join("datos", "lecturas_presion.csv")
    ruta_detalle = os.path.join("salidas", "reporte_detalle.csv")
    ruta_resumen = os.path.join("salidas", "reporte_resumen.csv")
    
    print("Leyendo datos...")
    filas = leer_csv(ruta_entrada)
    if not filas:
        print("No se encontraron datos o no se pudo leer el archivo.")
        return

    datos = filas[1:]
    lecturas_validas = []

    print("Procesando y validando filas")
    for fila in datos:
        if es_filaval(fila):
            id_lectura = fila[0].strip()
            estacion = fila[1].strip()
            presion_cruda = float(fila[2].strip())
            unidad = fila[3].strip()
            temporada = fila[4].strip()

            presion_hpa = convertir_a_hpa(presion_cruda, unidad)

            nueva_lectura = Lectura(id_lectura, estacion, presion_hpa, temporada)
            lecturas_validas.append(nueva_lectura)
    print("Generando reporte de detalle")
    lecturas_validas.sort(key=lambda x: x.id_lectura)
    
    datos_detalle = [["id_lectura", "estacion", "temporada", "presion_hpa", "nivel_presion"]]
    for loc in lecturas_validas:
        datos_detalle.append([
            loc.id_lectura,
            loc.estacion,
            loc.temporada,
            f"{loc.presion_hpa:.1f}",
            loc.clasificar()
        ])
    escribir_csv(ruta_detalle, datos_detalle)
    print("Generando reporte de resumen")
    agrupacion = {}
    
    for loc in lecturas_validas:
        temp = loc.temporada
        val = loc.presion_hpa
        
        if temp not in agrupacion:
            agrupacion[temp] = {'conteo': 0, 'suma': 0.0, 'maximo': float('-inf')}
        agrupacion[temp]['conteo'] += 1
        agrupacion[temp]['suma'] += val
        if val > agrupacion[temp]['maximo']:
            agrupacion[temp]['maximo'] = val

    lista_resumen = []
    for temp, metricas in agrupacion.items():
        promedio = metricas['suma'] / metricas['conteo']
        lista_resumen.append({
            'temporada': temp,
            'conteo': metricas['conteo'],
            'promedio': round(promedio, 1),
            'maximo': round(metricas['maximo'], 1)
        })

    lista_resumen.sort(key=lambda x: (-x['conteo'], x['temporada']))
    datos_resumen = [["temporada", "conteo", "promedio", "maximo"]]
    for item in lista_resumen:
        datos_resumen.append([
            item['temporada'],
            str(item['conteo']),
            f"{item['promedio']:.1f}",
            f"{item['maximo']:.1f}"
        ])
    escribir_csv(ruta_resumen, datos_resumen)
    print(f"¡Éxito! Se procesaron {len(lecturas_validas)} registros válidos.")
    print("Archivos generados en la carpeta 'salidas/'.")

if __name__ == "__main__":
    main()