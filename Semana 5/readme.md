# Perfilador de Datasets

Herramienta que analiza archivos CSV y genera reportes de calidad de datos.

## Requisitos
- Python 3.8 o superior

## Instalación

### 1. Clonar el repositorio

git clone [https://github.com/cesarGonzalez1/PCD_Gonzalez_Flores_Cesar]
cd Semana 5
### 2. Crear ambiente virtual:

python -m venv .venv
### 3. Activar ambiente virtual:
.venv\Scripts\activate

### 4. Instalar dependencias: 
pip install -r requirements.txt
### 5. UsoBash:
python main.py --input <archivo_entrada.csv> --output <archivo_salida.csv>
EjemploBash:
python main.py --input data/ventas.csv --output outputs/perfil_ventas.csv
python main.py --input data/sensores.csv --output outputs/perfil_sensores.csv
python main.py --input data/empleados.csv --output outputs/perfil_empleados.csv
### 6. Formato de Salida:
El perfil generado contiene las siguientes columnas:
Columna                    Descripción 
nombre_columna             Nombre de la columna
tipo_inferido              Tipo detectado (numerico/texto/fecha/booleano)
total_registros            Total de filas
valores_nulos              Cantidad de valores vacíos 
porcentaje_nulos           Porcentaje de nulos
valores_unicos             Cantidad de valores
distintosporcentaje_unicos Porcentaje de unicidad     
ejemplo_valor              Primer valor no nulo

Autor: Gonzalez Flores Cesar - Abril 2026