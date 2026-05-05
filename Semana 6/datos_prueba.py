
from typing import Dict

CODIGOS_PRUEBA = [
    # Productos
    "TEC-0001-MX",          # Válido
    "ALI-9999-US",          # Válido
    "ROB-1234-CA",          # Válido
    "tec-0001-MX",          # Inválido: minúsculas
    "TEC-001-MX",           # Inválido: solo 3 dígitos
    "TECH-0001-MX",         # Inválido: 4 letras en categoría

    # Envíos
    "ENV-2024-03-15-001234", # Válido
    "ENV-2025-12-01-999999", # Válido
    "ENV-2019-03-15-001234", # Inválido: año fuera de rango
    "ENV-2024-13-15-001234", # Inválido: mes 13
    "ENV-2024-03-32-001234", # Inválido: día 32

    # Empleados
    "EMP-VEN-1234",          # Válido
    "EMP-TEC-9999",          # Válido
    "EMP-ADM-1000",          # Válido
    "EMP-VEN-0123",          # Inválido: empieza con 0
    "EMP-XXX-1234",          # Inválido: departamento no válido
    "EMP-VEN-123",           # Inválido: solo 3 dígitos

    # Facturas
    "FAC-A-123456",          # Válido
    "FAC-E-000001",          # Válido
    "FAC-B-999999",          # Válido
    "FAC-F-123456",          # Inválido: serie F no existe
    "FAC-A-12345",           # Inválido: solo 5 dígitos
    "FAC-a-123456",          # Inválido: serie en minúscula

    # Desconocidos
    "XXX-1234",              # Desconocido
    "RANDOM-CODE",           # Desconocido
]
def mostrar_resultado(resultado: Dict) -> None:
    """Muestra el resultado de validación de un código de forma legible."""
    estado = "✓" if resultado["valido"] else "✗"
    print(f"{estado} {resultado['codigo']:<30} | Tipo: {resultado['tipo']:<12}")
    if resultado["valido"] and resultado["detalles"]:
        detalles = ", ".join(
            f"{k}: {v}" for k, v in resultado["detalles"].items() if v
        )
        print(f"   └── {detalles}")


def mostrar_reporte(reporte: Dict) -> None:
    """Muestra el reporte completo de procesamiento por lotes."""
    print("=" * 60)
    print("                 REPORTE DE VALIDACIÓN")
    print("=" * 60)
    print(f"\nTotal procesados: {reporte['total']}")
    print(f"Válidos:   {reporte['validos']} ({reporte['validos']/reporte['total']*100:.1f}%)")
    print(f"Inválidos: {reporte['invalidos']} ({reporte['invalidos']/reporte['total']*100:.1f}%)")

    print("\nDesglose por tipo:")
    print("-" * 40)
    for tipo, stats in reporte["por_tipo"].items():
        if stats["total"] > 0:
            tasa = stats["validos"] / stats["total"] * 100
            print(f"  {tipo.capitalize():<12}: {stats['validos']:>3}/{stats['total']:<3} ({tasa:.0f}% válidos)")

    print("\n" + "=" * 60)
