# main.py
# Script principal — ejecuta todas las partes del reto en orden

import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from validadores        import validar_producto, validar_envio, validar_empleado, validar_factura
from validador_universal import validar_codigo
from procesamiento      import procesar_lote
from datos_prueba       import CODIGOS_PRUEBA, mostrar_resultado, mostrar_reporte
from bonus              import sugerir_correccion, validar_fecha_real, exportar_resultados



print("\nPRUEBA DE FUNCIONES INDIVIDUALES")
print("=" * 50)

print("\n-- Productos --")
print(validar_producto("TEC-0001-MX"))
print(validar_producto("tec-0001-MX"))

print("\n-- Envíos --")
print(validar_envio("ENV-2024-03-15-001234"))
print(validar_envio("ENV-2024-13-15-001234"))

print("\n-- Empleados --")
print(validar_empleado("EMP-VEN-1234"))
print(validar_empleado("EMP-VEN-0123"))

print("\n-- Facturas --")
print(validar_factura("FAC-A-123456"))
print(validar_factura("FAC-F-123456"))


print("\n\nPRUEBA DE VALIDADOR UNIVERSAL")
print("=" * 50)

for codigo in CODIGOS_PRUEBA[:10]:   # primeros 10 códigos
    resultado = validar_codigo(codigo)
    mostrar_resultado(resultado)


print("\n\nPRUEBA DE PROCESAMIENTO POR LOTES")
reporte = procesar_lote(CODIGOS_PRUEBA)
mostrar_reporte(reporte)


print("\nBONUS")
print("=" * 50)

print("\n-- Sugerencias de corrección --")
invalidos_ejemplo = ["tec-0001-MX", "fac-a-123456", "TEC-001-MX", "EMP-VEN-0123"]
for cod in invalidos_ejemplo:
    sugerencia = sugerir_correccion(cod)
    print(f"  {cod:<25} → {sugerencia}")

print("\n-- Validación de fechas reales --")
fechas = [
    (2024, 2, 29),   
    (2023, 2, 29),   
    (2024, 4, 31),   
    (2025, 12, 31), 
]
for anio, mes, dia in fechas:
    valida = validar_fecha_real(anio, mes, dia)
    marca = "✓" if valida else "✗"
    print(f"  {marca} {anio}-{mes:02d}-{dia:02d}")

print("\n-- Exportar resultados a CSV --")
ruta_csv = os.path.join(os.path.dirname(__file__), "resultados", "reporte_validacion.csv")
exportar_resultados(reporte, ruta_csv)
